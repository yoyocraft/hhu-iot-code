#ifndef _QUICK_SORT_H_
#define _QUICK_SORT_H_

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/// @brief 在指定区间内进行划分，将比pivot小的元素放在pivot左边，比pivot大的元素放在右边。
/// @param arr 待排序数组
/// @param left 区间左端点
/// @param right 区间右端点
/// @return 划分出的pivot的下标
int partition(int *arr, int left, int right);

/// @brief 对指定区间进行快速排序
/// @param arr 待排序数组
/// @param left 排序区间左端点
/// @param right 排序区间右端点
void quick_sort(int *arr, int left, int right);

/// @brief 生成指定长度的随机整数数组
/// @param arr 要生成的随机数组
/// @param len 数组长度
void random_array(int *arr, int len);

#endif