import math
import time
from constants import *


# region class definition
class NeighborEntry:
    def __init__(self, depth, distance, time_received, invalid_time):
        self.depth = depth
        self.distance = distance
        self.time_received = time_received
        self.invalid_time = invalid_time


class Node:
    def __init__(self, id, depth, transmission_power, receiving_power_threshold):
        self.id = id
        self.depth = depth
        self.transmission_power = transmission_power
        self.receiving_power_threshold = receiving_power_threshold
        self.neighbor_table = {}  # Map of neighbor IDs to NeighborEntry
        self.type = "regular"  # regular, void, or trapped
        self.C_best = None
        self.time_Void = None
        self.EPA_max = 0


class ControlPacket:
    def __init__(
        self,
        node_id,
        nodetype,
        depth,
        initial_signal_strength=0,
        recRSSI=0,
        range_area=None,
        C_best=None,
    ):
        """
        初始化ControlPacket实例。

        :param node_id: 发送该包的节点ID
        :param nodetype: 节点类型，可以是'regular', 'void', 或 'trapped'
        :param depth: 节点的当前深度
        :param initial_signal_strength: （可选）初始信号强度，用于后续的距离计算
        :param recRSSI: （可选）接收到的信号强度指示，用于计算距离
        :param range_area: （可选）与路由相关的范围区域
        """
        self.node_id = node_id
        self.nodetype = nodetype
        self.depth = depth
        self.initial_signal_strength = initial_signal_strength
        self.recRSSI = recRSSI
        self.range_area = range_area
        self.C_best = C_best

    def to_bytes(self):
        """
        将ControlPacket对象转换为字节串，以便在网络中传输。
        这里简化处理，实际实现时需要考虑字节序和数据封装。
        """
        # 示例简单编码，实际应用中可能需要更复杂的序列化逻辑
        packet_data = f"{self.node_id}:{self.nodetype}:{self.depth}".encode()
        if self.initial_signal_strength is not None and self.recRSSI is not None:
            packet_data += f":{self.initial_signal_strength}:{self.recRSSI}".encode()
        return packet_data

    @staticmethod
    def from_bytes(bytes_data):
        """
        从字节串中解析出ControlPacket对象。
        """
        parts = bytes_data.decode().split(":")
        node_id, nodetype, depth = parts[:3]
        initial_signal_strength = None
        recRSSI = None
        if len(parts) > 3:
            initial_signal_strength, recRSSI = map(float, parts[3:])
        return ControlPacket(
            int(node_id), nodetype, float(depth), initial_signal_strength, recRSSI, 100
        )


# endregion

# region update phase


def update_phase(node, pkt):
    """
    更新阶段的核心逻辑，处理接收到的控制包，更新邻居表，计算EPA，以及根据情况调整节点状态。

    :param node: 当前处理消息的节点实例
    :param pkt: 接收到的控制包实例
    """

    global nodes  # 用于可能的广播操作

    # 获取发送节点的深度和当前节点的深度
    dp = pkt.depth
    dc = node.depth

    if pkt.initial_signal_strength is None or pkt.recRSSI is None:
        print("Error: Unable to calculate distance. Skipping EPA computation.")
        return

    # 计算接收到该控制包的节点与发送节点之间的距离
    distance_to_pkt_sender = calculate_distance(
        pkt.initial_signal_strength, pkt.recRSSI
    )

    # 检查距离计算是否成功
    if distance_to_pkt_sender is None:
        print("Error: Unable to calculate distance. Skipping EPA computation.")
        return  # 如果无法计算距离，则直接结束本次更新处理

    # 处理来自常规节点的控制包
    if pkt.nodetype == "regular":
        # 设置空洞检测定时器的触发时间
        time_inV = time.time() + T_inV

        # 更新邻居表，记录接收到的包的发送节点信息
        node.neighbor_table[pkt.node_id] = NeighborEntry(
            dp, distance_to_pkt_sender, time.time(), time_inV
        )

        # 如果接收到的节点深度小于当前节点深度
        if dp < dc:
            # 计算预期包推进(EPA)，用于评估转发该节点的效益
            EPA = compute_EPA(distance_to_pkt_sender, dp - dc)
            # 如果计算出的EPA优于当前最佳值，则更新C_best和EPA_max
            if EPA > node.EPA_max:
                node.EPA_max = EPA
                node.C_best = pkt.node_id  # 记录最佳转发候选节点ID

    # 处理来自空洞或受困节点的控制包
    elif pkt.nodetype in ["void", "trapped"]:
        # 从邻居表中移除发送该包的节点，因为它已标识为不可达或问题节点
        node.neighbor_table.pop(pkt.node_id, None)

        # 重新评估当前节点状态，检查是否有更深的正常邻居
        remaining_neighbors = {
            n_id: n_info
            for n_id, n_info in node.neighbor_table.items()
            if n_info.depth < node.depth
        }

        # 如果没有比当前节点深度更低的邻居
        if not remaining_neighbors:
            # 将当前节点标记为空洞
            node.type = "void"
            broadcast_control_pkt_as_void(node)  # 广播报文通知其他节点此节点变为空洞

        # 如果所有比当前节点深度低的邻居都是空洞或受困
        elif all(
            n_type in ["void", "trapped"] for n_type in remaining_neighbors.values()
        ):
            # 将当前节点标记为受困
            node.type = "trapped"
            broadcast_control_pkt_as_trapped(node)  # 广播报文通知其他节点此节点受困

    # 在当前逻辑中，如果节点不是从 "void" 或 "trapped" 类型接收到消息，则无需额外操作，维持当前状态
    else:
        pass


def calculate_distance(initial_signal_strength, received_rssi):
    # 使用Thorp模型或其他合适模型计算距离, Mock
    return (
        (initial_signal_strength - received_rssi) / (2 * SPEED_OF_SOUND * ALPHA) * 1000
    )


def compute_pe(distance, avg_snr=10):
    """
    计算包错误概率。
    :param distance: 两点之间的距离（单位：米）
    :param avg_snr: 平均信噪比
    :return: 包错误概率
    """
    packet_size_bits = 8  # 假设每个数据包大小为8位
    # 使用论文中提到的模型计算比特错误概率，然后转化为包错误概率
    bit_error_probability = 0.5 * (1 - math.sqrt(avg_snr / (1 + avg_snr)))
    # 假设一个数据包有n位，这里简化处理，不直接使用n
    packet_delivery_probability = (
        1 - bit_error_probability
    ) ** packet_size_bits  # 假设packet_size_bits为数据包大小
    return 1 - packet_delivery_probability  # 包错误概率是1减去包交付概率


def compute_EPA(distance, depth_difference, avg_snr=10):
    """
    计算预期包推进（EPA）值。
    EPA反映了数据包向网络出口方向推进的效益，它基于深度差异和考虑了距离相关的包错误概率。

    :param distance: 当前节点到目标节点的估计物理距离（单位：米）
    :param depth_difference: 当前节点与目标节点之间的深度差（单位：米）
    :param avg_snr: 当前链路的平均信噪比
    :return: 预期包推进（EPA）值，用于评估数据包的转发效益
    """
    # P = compute_pe(distance, avg_snr)  # 计算包错误概率
    # EPA = P * depth_difference  # 根据论文公式计算EPA
    # return EPA
    return distance + depth_difference + avg_snr * ALPHA  # mock handler


def broadcast_control_pkt_as_void(node):
    """
    构造并广播一个标识节点状态为"void"的控制包。
    当节点发现其下方没有活跃的邻居，即成为"void"节点时，此函数会被调用，
    用于通知网络中的其他节点当前节点的状态变化。

    :param node: 当前节点的实例，其状态将被设置为"void"
    """
    pkt = ControlPacket(node.id, "void", node.depth)  # 创建标识为"void"的控制包
    broadcast(pkt)  # 调用实际的广播逻辑进行数据包发送


def broadcast_control_pkt_as_trapped(node):
    """
    构造并广播一个标识节点状态为"trapped"的控制包。
    当节点发现所有比它深度低的邻居都是"void"或"trapped"状态时，
    此函数用于通知网络该节点现在处于"trapped"状态。

    :param node: 当前节点的实例，其状态将被设置为"trapped"
    """
    pkt = ControlPacket(node.id, "trapped", node.depth)  # 创建标识为"trapped"的控制包
    broadcast(pkt)  # 调用实际的广播逻辑进行数据包发送


def broadcast(pkt):
    """
    实际执行的广播逻辑，替换原先的占位符函数。
    应该实现具体的网络通信逻辑，将控制包发送至网络中的其他节点。
    目前仍使用模拟打印作为示例。

    :param pkt: 要广播的控制包实例
    """
    # 此处应添加实现真实网络广播的代码，如使用UDP套接字发送数据包
    print(
        f"Simulated Broadcasting control packet from node {pkt.node_id} with type '{pkt.nodetype}'."
    )
    # 实际应用中，这行模拟输出应被实际的网络发送代码替代


# endregion

# region routing phase


def routing_phase(node, pkt):
    """
    路由阶段的核心逻辑，根据SORP算法原理决定数据包的转发或丢弃。

    :param node: 当前处理数据包的节点
    :param pkt: 待处理的数据包
    """
    global nodes  # 引用全局节点列表，便于访问或更新其他节点信息

    # 获取数据包和当前节点的关键参数
    dp = pkt.depth  # 数据包来源节点深度
    dc = node.depth  # 当前节点的深度
    range_area = pkt.range_area  # 数据包允许的最大转发范围
    ID_b = pkt.C_best  # 数据包标识的最佳转发候选节点ID

    # 确定当前节点到最佳候选节点的距离
    dist_i_ID_b = get_distance(node.id, ID_b, node.neighbor_table)

    # 检查转发条件：
    # 1. 当前节点深度必须低于数据包来源节点深度（表明数据包正向上传）；
    # 2. 节点状态为 "regular"，即不是空洞或受困状态；
    # 3. 到最佳候选节点的距离在允许的转发范围内。
    # 如果以上条件满足，则继续转发流程
    if (
        dc < dp
        and node.type == "regular"
        and dist_i_ID_b is not None
        and dist_i_ID_b <= range_area
    ):
        # 寻找下一个深度更低且距离合适的转发节点
        dn = search_dn(node, range_area)
        if dn is not None:  # 确保找到了有效的下一跳节点
            # 计算数据包的持有时间，基于当前节点与下一跳节点的深度差，以优化转发时机
            T_hold = calculate_T_hold(dc, dn.depth)
            # 设置定时器，准备在T_hold时间后转发数据包
            set_forwarding_timer(node, T_hold)
        else:
            # 如果没有找到合适的下一跳节点，尽管满足其他条件，也应丢弃数据包
            drop_packet(pkt)
    else:
        # 不满足转发条件（深度、状态或距离限制），直接丢弃数据包
        drop_packet(pkt)


def get_distance(current_id, target_id, neighbor_table):
    """
    根据邻居表，获取当前节点到目标节点的距离。
    如果目标节点不在邻居表中，则返回无穷大，表示距离不可达。

    :param current_id: 当前节点ID
    :param target_id: 目标节点ID
    :param neighbor_table: 当前节点的邻居表，格式为{node_id: NeighborEntry}
    :return: 当前节点到目标节点的距离，未找到则返回无穷大
    """
    if target_id in neighbor_table:
        return neighbor_table[target_id].distance
    return float("inf")


def search_dn(node, range_area):
    """
    在当前节点的邻居中搜索下一个深度更低的转发候选节点，且距离需在指定范围内。
    选择的标准是深度最低且距离最近的节点。

    :param node: 当前节点对象
    :param range_area: 转发范围限制
    :return: 下一跳节点ID，如果没有合适的节点则返回None
    """
    candidates = [
        (n_id, n_info.depth, n_info.distance)
        for n_id, n_info in node.neighbor_table.items()
        if n_info.depth < node.depth and n_info.distance <= range_area
    ]
    # 选择深度最低且距离最近的节点
    if candidates:
        return min(candidates, key=lambda x: (x[1], x[2]))[0]  # 根据深度和距离排序
    return None


def calculate_T_hold(current_depth, next_depth):
    """
    根据当前节点和下一跳节点的深度差计算数据包的持有时间。
    持有时间帮助优化数据包的转发时机，减少冲突和提高传输效率。

    :param current_depth: 当前节点深度
    :param next_depth: 下一跳节点深度
    :return: 数据包的持有时间（秒）
    """
    # 假设基于深度差直接线性计算，实际应用中可能涉及更多因素
    return (next_depth - current_depth) / SPEED_OF_SOUND


def set_forwarding_timer(node, timeout):
    """
    设置一个定时器，用于在指定时间后执行数据包的转发操作。
    这是一个占位符函数，实际实现可能依赖于特定的异步框架或操作系统API。

    :param node: 当前节点对象
    :param timeout: 定时器超时时间（秒）
    """
    print(f"Setting forwarding timer for node {node.id} to {timeout} seconds.")
    # 实际实现应包含具体定时器逻辑，例如使用threading.Timer或asyncio.sleep


def drop_packet(packet):
    """
    处理需要丢弃的数据包，可能包括日志记录或其他资源清理操作。

    :param packet: 需要丢弃的数据包对象
    """
    print(f"Dropping packet from node {packet.node_id}.")
    # 实际应用中可能需要更多的处理逻辑，如统计丢包率、释放相关资源等


# endregion
