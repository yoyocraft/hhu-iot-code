#include <stdio.h>

#define COLOR(a, b) "\033[" #b "m" a "\033[0m"
#define GREEN(a) COLOR(a, 32)
#define RED(a) COLOR(a, 31)

#define MAX_MAZE_SIZE 100

typedef struct
{
    int x, y; // 格子坐标
} Position;

Position stack[MAX_MAZE_SIZE * MAX_MAZE_SIZE];
int top = -1;

// 迷宫地图
int maze[MAX_MAZE_SIZE][MAX_MAZE_SIZE];

// 标记数组，用于记录哪些格子已经访问过
int visited[MAX_MAZE_SIZE][MAX_MAZE_SIZE];

/// @brief 入栈
void push(int x, int y)
{
    top++;
    stack[top].x = x;
    stack[top].y = y;
}

/// @brief 出栈
void pop()
{
    top--;
}

/// @brief 返回栈顶元素
Position peek()
{
    return stack[top];
}

/// @brief 判断当前位置是否是终点
int isEndPosition(int x, int y, int n, int m)
{
    return (x == n - 1) && (y == m - 1);
}

/// @brief 校验坐标(x, y)是否可行
///         坐标在可行范围内 && 无障碍 && 没有被访问过
int checkValid(int x, int y, int n, int m)
{
    return x >= 0 && x < n && y >= 0 && y < m && !maze[x][y] && !visited[x][y];
}

/// @brief 深度优先搜索迷宫，从起点开始，依次遍历相邻的通道，直到找到终点或者无路可走。
///        如果找到了终点，则将路径上的位置信息存储在栈中。
int dfs(int startX, int startY, int n, int m)
{
    // 将起点入栈，并标记为已经访问过
    push(startX, startY);
    visited[startX][startY] = 1;

    // 取出栈顶元素，作为当前位置
    Position current = peek();
    if (isEndPosition(current.x, current.y, n, m))
        return 1;

    // 枚举四个方向 (枚举策略：下->右->上->左)
    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, 1, 0, -1};
    for (int i = 0; i < 4; i++)
    {
        int newX = current.x + dx[i];
        int newY = current.y + dy[i];

        // 如果该方向可以走，则将新位置入栈，并标记为已经访问过
        if (checkValid(newX, newY, n, m))
        {
            push(newX, newY);
            visited[newX][newY] = 1;
            // 递归
            if (dfs(newX, newY, n, m))
                return 1;
            // 回溯
            pop();
            visited[newX][newY] = 0;
        }
    }
    // 四个方向皆不可行
    return 0;
}

void printPath(int n, int m)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (visited[i][j])
            {
                printf(GREEN("%d "), maze[i][j]);
                continue;
            }
            printf("%d ", maze[i][j]);
        }
        printf("\n");
    }
}

/*
【测试数据1：能找到路径】
10 10
0 1 0 0 0 1 0 1 0 0
0 0 0 1 0 0 0 1 0 1
0 1 0 1 0 1 0 0 0 0
0 0 0 0 1 0 1 0 1 0
0 1 0 1 0 0 0 0 0 1
0 0 0 0 0 1 0 1 0 0
0 1 0 1 0 0 0 0 1 0
0 1 0 0 0 1 0 0 0 1
1 0 0 1 0 1 0 0 0 0
1 1 0 0 0 0 0 1 1 0

【测试数据2：不能找到路径】
10 10
0 1 0 0 0 1 0 1 0 0
0 0 0 1 0 0 0 1 0 1
0 1 0 1 0 1 0 0 0 0
0 0 0 0 1 0 1 0 1 0
0 1 0 1 0 0 0 0 0 1
0 0 0 0 0 1 0 1 0 0
0 1 0 1 0 0 0 0 1 0
0 1 0 0 0 1 0 0 0 1
1 0 0 1 0 1 0 0 0 1
1 1 0 0 0 0 0 1 1 0
*/
int main(int argc, char const *argv[])
{
    // 输入迷宫地图
    int n, m;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf("%d", &maze[i][j]);
        }
    }

    // 求解迷宫问题
    int startX = 0, startY = 0;
    int result = dfs(startX, startY, n, m);
    if (!result)
    {
        printf(RED("无法找到终点!\n"));
        return 1;
    }
    // 输出路径
    printf(GREEN("找到终点!\n"));
    printPath(n, m);
    return 0;
}