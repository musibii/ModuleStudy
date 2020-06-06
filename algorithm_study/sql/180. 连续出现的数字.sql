# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : 180. 连续出现的数字.sql
# __time__  : 2020/6/6 11:56 下午
-- 编写一个 SQL 查询，查找所有至少连续出现三次的数字。
--
-- +----+-----+
-- | Id | Num |
-- +----+-----+
-- | 1  |  1  |
-- | 2  |  1  |
-- | 3  |  1  |
-- | 4  |  2  |
-- | 5  |  1  |
-- | 6  |  2  |
-- | 7  |  2  |
-- +----+-----+
-- 例如，给定上面的 Logs 表， 1 是唯一连续出现至少三次的数字。
--
-- +-----------------+
-- | ConsecutiveNums |
-- +-----------------+
-- | 1               |
-- +-----------------+
--
-- 来源：力扣（LeetCode）
-- 链接：https://leetcode-cn.com/problems/consecutive-numbers
-- 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Write your MySQL query statement below
-- select Num as ConsecutiveNums from Logs group by Num having count(Num) >= 3;

SELECT *
FROM
    Logs l1,
    Logs l2,
    Logs l3
WHERE
    l1.Id = l2.Id - 1
    AND l2.Id = l3.Id - 1
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num
;