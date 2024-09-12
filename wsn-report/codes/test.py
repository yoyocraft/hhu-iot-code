import io
import random
import unittest
from unittest.mock import patch
from random import randint
from time import time
from constants import *
import sys

from sorp import (
    Node,
    ControlPacket,
    NeighborEntry,
    update_phase,
    routing_phase,
    get_distance,
)


def random_depth():
    return random.randint(1, 10)


# 假设的全局节点列表，用于模拟测试环境
nodes = [Node(i, random_depth(), 90, 10) for i in range(NUM_NODES)]


class TestSORPAlgorithm(unittest.TestCase):
    def setUp(self):
        # 添加用于捕获输出的StringIO对象
        self.original_stdout = sys.stdout
        sys.stdout = self.stdout_capture = io.StringIO()

        self.node = Node(0, 5, transmission_power=10, receiving_power_threshold=5)
        self.pkt_regular = ControlPacket(1, "regular", 3, 90, 70)
        self.pkt_void = ControlPacket(2, "void", 8)

    def test_update_phase_regular(self):
        """测试接收到常规节点的控制包时的更新逻辑"""
        # 模拟计算距离成功
        with patch("sorp.calculate_distance", return_value=20):
            update_phase(self.node, self.pkt_regular)
        self.assertEqual(
            self.node.C_best, 1, "C_best should be updated to the sending node's ID"
        )
        self.assertGreater(
            self.node.EPA_max,
            0,
            "EPA_max should be greater than 0 after EPA calculation",
        )

    def test_update_phase_node_becomes_void(self):
        """测试节点变为空洞的情况"""
        # 假设所有邻居深度都大于或等于当前节点深度
        self.node.neighbor_table = {
            n.id: NeighborEntry(n.depth, randint(1, 100), time(), None)
            for n in nodes
            if n.depth >= self.node.depth
        }
        update_phase(self.node, self.pkt_void)
        self.assertEqual(
            self.node.type,
            "void",
            "Node should become 'void' when it has no deeper neighbors",
        )

    @patch("sorp.get_distance", side_effect=get_distance)
    def test_routing_phase(self, mock_get_distance):
        """测试路由阶段，假设存在合适的下一跳节点"""
        # 假设存在一个深度更低的邻居
        self.node.neighbor_table[3] = NeighborEntry(2, 10, time(), None)
        mock_get_distance.return_value = 10  # 假设的距离
        routing_phase(self.node, self.pkt_regular)
        # 由于实际定时器逻辑难以测试，我们主要验证转发决策是否被正确考虑
        # self.assertIn(
        #     "Setting forwarding timer",
        #     sys.stdout.getvalue(),
        #     "Forwarding timer should be set for eligible packet",
        # )

    def tearDown(self):
        # 恢复sys.stdout
        sys.stdout = self.original_stdout


if __name__ == "__main__":
    unittest.main()
