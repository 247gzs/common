# -*- coding: utf-8 -*-
from typing import Optional, Any

from aredis import StrictRedis


class StringMixin:

    async def set(self, key: str, value: str) -> bool:
        """
        设置指定 key 的值
        """
        return await self.redis_client.set(key, value)

    async def get(self, key: str) -> bytes:
        """
        获取指定 key 的值
        """
        return await self.redis_client.get(key)

    async def incr(self, name: str, amount=1) -> int:
        """
        将 key 中储存的数字值增一
        """
        return await self.redis_client.incr(name, amount=amount)

    async def decr(self, name: str, amount=1) -> int:
        """
        将 key 中储存的数字值减一
        """
        return await self.redis_client.decr(name, amount=amount)

    async def append(self, key: str, value: str) -> int:
        """
        如果 key 已经存在并且是一个字符串，append 命令将指定的 value 追加到该 key 原来值（value）的末尾
        """
        return await self.redis_client.append(key, value)

    async def strlen(self, name: str) -> int:
        """
        返回 key 所储存的字符串值的长度
        """
        return await self.redis_client.strlen(name)

    async def setex(self, name: str, time: int, value: str) -> bool:
        """
        将值 value 关联到 name ，并将 name 的过期时间设为 seconds (以秒为单位)
        """
        return await self.redis_client.setex(name, time, value)

    async def setnx(self, name: str, value: str) -> bool:
        """
        只有在 key 不存在时设置 key 的值
        """
        return await self.redis_client.setnx(name, value)


class ListMixin:

    async def lpush(self, key: str, *values) -> int:
        """
        将一个或多个值插入到列表头部

        返回的是列表中的数据量
        """
        return await self.redis_client.lpush(key, *values)

    async def lpop(self, name: str) -> bytes:
        """
        移出并获取列表的第一个元素
        """
        return await self.redis_client.lpop(name)

    async def lrange(self, name: str, start: int, end: int) -> list:
        """
        获取列表指定范围内的元素
        """
        return await self.redis_client.lrange(name, start, end)

    async def llen(self, name: str) -> int:
        """
        获取列表长度
        """
        return await self.redis_client.llen(name)

    async def lrem(self, name, count, value) -> int:
        """
        移除列表元素

        count > 0 : 从表头开始向表尾搜索，移除与 value 相等的元素，数量为 count
        count < 0 : 从表尾开始向表头搜索，移除与 value 相等的元素，数量为 count 的绝对值
        count = 0 : 移除表中所有与 value 相等的值
        """
        return await self.redis_client.lrem(name, count, value)

    async def ltrim(self, name, start, end) -> bool:
        """
        对一个列表进行修剪(trim)，列表只保留指定区间内的元素，不在指定区间之内的元素都将被删除。
        """
        return await self.redis_client.ltrim(name, start, end)

    async def lpushx(self, name: str, value: str) -> int:
        """
        将一个值插入到已存在的列表头部
        """
        return await self.redis_client.lpushx(name, value)

    async def rpop(self, name: str) -> int:
        """
        用于移除列表的最后一个元素，返回值为移除的元素
        """
        return await self.redis_client.rpop(name)

    async def rpush(self, name: str, *values) -> int:
        """
        在列表中添加一个或多个值，返回列表中元素数量
        """
        return await self.redis_client.rpush(name, *values)

    async def rpushx(self, name: str, value: str) -> int:
        """
        用于将一个值插入到已存在的列表尾部（最右边）。如果列表不存在，操作无效
        """
        return await self.redis_client.rpushx(name, value)

    async def linsert(self, name: str, where: str, refvalue: str, value: str) -> int:
        """
        用于在列表的元素前或者后插入元素。
            当指定元素不存在于列表中时，不执行任何操作
            当列表不存在时，被视为空列表，不执行任何操作
            如果 name 不是列表类型，返回一个错误
        :return:
            如果命令执行成功，返回插入操作完成之后，列表的长度
            如果没有找到指定元素 ，返回 -1
            如果 name 不存在或为空列表，返回 0
        """
        return await self.redis_client.linsert(name, where, refvalue, value)

    async def lindex(self, name: str, index: int) -> str:
        """
        通过索引获取列表中的元素
            可以使用负数下标，以 -1 表示列表的最后一个元素， -2 表示列表的倒数第二个元素，以此类推
        :return:
            列表中下标为指定索引值的元素
                如果指定索引值不在列表的区间范围内，返回 nil
        """
        return await self.redis_client.lindex(name, index)

    async def blpop(self, keys: list, timeout=0) -> str:
        """
        移出并获取列表的第一个元素， 如果列表没有元素会阻塞列表直到等待超时或发现可弹出元素为止。
        """
        return await self.redis_client.blpop(keys, timeout)

    async def brpop(self, keys: list, timeout=0) -> str:
        """
        移出并获取列表的第一个元素， 如果列表没有元素会阻塞列表直到等待超时或发现可弹出元素为止。
        """
        return await self.redis_client.brpop(keys, timeout)


class SetMixin:

    async def sadd(self, name: str, *values) -> int:
        """
        向集合添加一个或多个成员，已经存在于集合的成员元素将被忽略。

        :return
            被添加到集合中的新元素的数量，不包括被忽略的元素
        """
        return await self.redis_client.sadd(name, *values)

    async def scard(self, name: str):
        """
        获取集合的成员数
        :return:
            集合的数量。 当集合 key 不存在时，返回 0
        """
        return await self.redis_client.scard(name)

    async def sdiff(self, keys: list, *args):
        """
        :return
            返回第一个集合与其他集合之间的差异
        """
        return await self.redis_client.sdiff(keys, *args)

    async def sdiffstore(self, dest: str, keys: list, *args):
        """
        :return
            返回给定所有集合的差集并存储在 dest 中
        """
        return await self.redis_client.sdiffstore(dest, keys, *args)

    async def sinter(self, keys: list, *args):
        """
        :return:
            返回给定所有集合的交集
        """
        return await self.redis_client.sinter(keys, *args)

    async def sinterstore(self, dest: str, keys: list, *args):
        """
        :return:
            返回给定所有集合的交集并存储在 dest 中
        """
        return await self.sinterstore(dest, keys, *args)

    async def sismember(self, name: str, value: str) -> int:
        """
        判断 member 元素是否是集合 key 的成员
        :return:
            如果成员元素是集合的成员，返回 1
            如果成员元素不是集合的成员，或 key 不存在，返回 0
        """
        return await self.redis_client.sismember(name, value)

    async def smembers(self, name) -> list:
        """
        :return:
            返回集合中的所有成员
        """
        return await self.redis_client.smembers(name)

    async def smove(self, src: str, dst: str, value: str) -> int:
        """
        将 value 元素从 src 集合移动到 dst 集合
        :return:
            如果成员元素被成功移除，返回 1 。 如果成员元素不是 source 集合的成员，并且没有任何操作对 destination 集合执行，那么返回 0
        """
        return await self.redis_client.smove(src, dst, value)

    async def spop(self, name, count=None):
        """
        移除并返回集合中的一个随机元素
        :return:
            被移除的随机元素。 当集合不存在或是空集时，返回 nil
        """
        return await self.redis_client.spop(name, count=count)

    async def srandmember(self, name: str, number=None) -> list:
        """
        :return:
            返回集合中一个或多个随机元素
        """
        return await self.redis_client.srandmember(name, number=number)

    async def srem(self, name: str, *values) -> int:
        """
        移除集合中一个或多个成员
        :return:
            被成功移除的元素的数量，不包括被忽略的元素
        """
        return await self.redis_client.srem(name, *values)

    async def sunion(self, keys: list, *args) -> list:
        """
        返回所有给定集合的并集
        :return:
            并集成员的列表
        """
        return await self.redis_client.sunion(keys, *args)

    async def sunionstore(self, dest: str, keys: list, *args) -> int:
        """
        所有给定集合的并集存储在 dest 集合中
        :return:
            结果集中的元素数量
        """
        return await self.redis_client.sunionstore(dest, keys, *args)

    async def sscan(self, name: str, cursor=0, match=None, count=None) -> list:
        """
        迭代集合中的元素
        :return:
            数组列表
        """
        return await self.redis_client.sscan(name, cursor=cursor, match=match, count=count)


class HashMixin:

    async def hdel(self, name: str, *keys) -> int:
        """
        删除哈希表 key 中的一个或多个指定字段，不存在的字段将被忽略
        :return:
            被成功删除字段的数量，不包括被忽略的字段
        """
        return await self.redis_client.hdel(name, *keys)

    async def hexists(self, name: str, key: str) -> int:
        """
        查看哈希表 key 中，指定的字段是否存在
        :return:
            如果哈希表含有给定字段，返回 1
            如果哈希表不含有给定字段，或 key 不存在，返回 0
        """
        return await self.redis_client.hexists(name, key)

    async def hget(self, name: str, key: str) -> str:
        """
        获取存储在哈希表中指定字段的值
        :return:
            返回给定字段的值。如果给定的字段或 key 不存在时，返回 nil
        """
        return await self.redis_client.hget(name, key)

    async def hgetall(self, name: str) -> list:
        """
        获取在哈希表中指定 key 的所有字段和值
        :return:
            以列表形式返回哈希表的字段及字段值。 若 key 不存在，返回空列表
        """
        return await self.redis_client.hgetall(name)

    async def hincrby(self, name: str, key: str, amount=1) -> str:
        """
        为哈希表中的字段值加上指定增量值
        增量也可以为负数，相当于对指定字段进行减法操作
        如果哈希表的 key 不存在，一个新的哈希表被创建并执行 HINCRBY 命令
        如果指定的字段不存在，那么在执行命令前，字段的值被初始化为 0
        对一个储存字符串值的字段执行 HINCRBY 命令将造成一个错误
        :return:
            执行 HINCRBY 命令之后，哈希表中字段的值
        """
        return await self.redis_client.hincrby(name, key, amount=amount)

    async def hincrbyfloat(self, name: str, key: str, amount=1.0) -> str:
        """
        为哈希表中的字段值加上指定浮点数增量值
        如果指定的字段不存在，那么在执行命令前，字段的值被初始化为 0

        其他说明参考： hincrby
        """
        return await self.redis_client.hincrbyfloat(name, key, amount=amount)

    async def hkeys(self, name: str) -> list:
        """
        获取所有哈希表中的字段
        :return:
            包含哈希表中所有域（field）列表。 当 key 不存在时，返回一个空列表
        """
        return await self.redis_client.hkeys(name)

    async def hlen(self, name: str) -> int:
        """
        获取哈希表中字段的数量
        :return:
            哈希表中字段的数量。 当 key 不存在时，返回 0
        """
        return await self.redis_client.hlen(name)

    async def hset(self, name: str, key: str, value: str) -> int:
        """
        将哈希表 key 中的字段 field 的值设为 value

        如果哈希表不存在，一个新的哈希表被创建并进行 HSET 操作
        如果字段已经存在于哈希表中，旧值将被覆盖
        :return:
            如果字段是哈希表中的一个新建字段，并且值设置成功，返回 1
            如果哈希表中域字段已经存在且旧值已被新值覆盖，返回 0
        """
        return await self.redis_client.hset(name, key, value)

    async def hsetnx(self, name: str, key: str, value: str) -> int:
        """
        只有在字段 field 不存在时，设置哈希表字段的值

        如果哈希表不存在，一个新的哈希表被创建并进行 HSET 操作
        如果字段已经存在于哈希表中，操作无效
        如果 key 不存在，一个新哈希表被创建并执行 HSETNX 命令
        :return:
            设置成功，返回 1
            如果给定字段已经存在且没有操作被执行，返回 0
        """
        return await self.redis_client.hsetnx(name, key, value)

    async def hmset(self, name: str, mapping: dict) -> str:
        """
        同时将多个 field-value (域-值)对设置到哈希表 key 中

        此命令会覆盖哈希表中已存在的字段
        如果哈希表不存在，会创建一个空哈希表，并执行 HMSET 操作
        :return:
            如果命令执行成功，返回 OK
        """
        return await self.redis_client.hmset(name, mapping)

    async def hmget(self, name: str, keys: list, *args) -> list:
        """
        用于返回哈希表中，一个或多个给定字段的值
        如果指定的字段不存在于哈希表，那么返回一个 nil 值
        :return:
            一个包含多个给定字段关联值的表，表值的排列顺序和指定字段的请求顺序一样
        """
        return await self.redis_client.hmget(name, keys, *args)

    async def hvals(self, name: str) -> list:
        """
        获取哈希表中所有值
        :return:
            一个包含哈希表中所有值的列表。 当 key 不存在时，返回一个空表
        """
        return await self.redis_client.hvals(name)

    async def hscan(self, name: str, cursor=0, match=None, count=None) -> list:
        """
        迭代哈希表中的键值对
        :return:
            返回的每个元素都是一个元组，每一个元组元素由一个字段(field) 和值（value）组成
        """
        return await self.redis_client.hscan(name, cursor=cursor, match=match, count=count)

    async def hstrlen(self, name: str, key: str) -> int:
        """
        获取哈希表 key 中， 与给定域 field 相关联的值的字符串长度（string length）
        如果给定的键或者域不存在， 那么命令返回 0
        """
        return await self.redis_client.hstrlen(name, key)


class ZSetMixin:

    async def zadd(self, name: str, *args, **kwargs) -> int:
        """
        向有序集合添加一个或多个成员，或者更新已存在成员的分数

        如果某个成员已经是有序集的成员，那么更新这个成员的分数值，并通过重新插入这个成员元素，来保证该成员在正确的位置上
        分数值可以是整数值、双精度浮点数、-inf、+inf
        如果有序集合 key 不存在，则创建一个空的有序集并执行 ZADD 操作
        当 key 存在但不是有序集类型时，返回一个错误
        :return:
            被成功添加的新成员的数量，不包括那些被更新的、已经存在的成员
        """
        return await self.redis_client.zadd(name, *args, **kwargs)

    async def zaddoption(self, name: str, option: str, *args, **kwargs) -> int:
        """
        相关说明参考： zadd
        :param name:
            key 名称
        :param option:
            XX: 仅仅更新存在的成员，不添加新成员
            NX: 不更新存在的成员。只添加新成员
            CH: 修改返回值为发生变化的成员总数，原始是返回新添加成员的总数 (CH 是 changed 的意思)。
                更改的元素是新添加的成员，已经存在的成员更新分数。 所以在命令中指定的成员有相同的分数将不被计算在内。
                注：在通常情况下，ZADD返回值只计算新添加成员的数量。
            INCR: 当ZADD指定这个选项时，成员的操作就等同ZINCRBY命令，对成员的分数进行递增操作
        :param args:
            以列表形式指定的待添加成员信息
        :param kwargs:
            以字典形式执行的待添加成员信息
        :return:
            返回满足 option所属条件 的成员数量
        """
        return await self.redis_client.zaddoption(name, option=option, *args, **kwargs)

    async def zcard(self, name: str) -> int:
        """
        获取有序集合的成员数
        :return:
            当 name 存在且是有序集类型时，返回有序集的基数。 当 name 不存在时，返回 0
        """
        return await self.redis_client.zcard(name)

    async def zcount(self, name: str, min: Optional[Any], max: Optional[Any]) -> int:
        """
        计算在有序集合中指定区间分数的成员数
        :return:
            分数值在 min 和 max 之间的成员的数量
        """
        return await self.redis_client.zcount(name, min, max)

    async def zincrby(self, name: str, value: str, amount=1) -> str:
        """
        有序集合中对指定成员的分数加上增量 amount

        可以通过传递一个负数值 amount ，让分数减去相应的值，比如 ZINCRBY key -5 member ，就是让 member 的 score 值减去 5
        当 key 不存在，或分数不是 key 的成员时， ZINCRBY key amount member 等同于 ZADD key amount member
        当 key 不是有序集类型时，返回一个错误
        分数值可以是整数值或双精度浮点数
        :return:
            member 成员的新分数值，以字符串形式表示
        """
        return await self.redis_client.zincrby(name, value, amount=amount)

    async def zinterstore(self, dest: str, keys: list, aggregate=None) -> int:
        """
        计算给定的一个或多个有序集的交集并将结果集存储在新的有序集合 dest 中

        默认情况下，结果集中某个成员的分数值是所有给定集下该成员分数值之和
        :return:
            保存到目标结果集的的成员数量
        """
        return await self.redis_client.zinterstore(dest, keys, aggregate=aggregate)

    async def zlexcount(self, name: str, min: Optional[Any], max: Optional[Any]) -> int:
        """
        在有序集合中计算指定字典区间内成员数量
        :return:
            指定区间内的成员数量
        """
        return await self.redis_client.zlexcount(name, min, max)

    async def zrange(
            self, name: str, start: int, end: int,
            desc=False, with_scores=False, score_cast_func=float
    ) -> list:
        """
        通过索引区间返回有序集合指定区间内的成员

        其中成员的位置按分数值递增（从小到大）来排序
        具有相同分数值的成员按字典序（lexicographical order）来排列
        如果你需要成员按值递减（从大到小）来排列，请使用 ZREVRANGE 命令
        下标参数 start 和 stop 都以 0 为底，也就是说，以 0 表示有序集第一个成员，以 1 表示有序集第二个成员，以此类推
        你也可以使用负数下标，以 -1 表示最后一个成员， -2 表示倒数第二个成员，以此类推

        :param with_scores: 输出结果中是否包含分数
        :param score_cast_func: score输出类型： int or float
        :return:
            指定区间内，带有分数值（可选）的有序集成员的列表
        """
        return await self.redis_client.zrange(
            name, start, end, desc=desc, withscores=with_scores, score_cast_func=score_cast_func
        )

    async def zrangebylex(self, name: str, min: str, max: str, start=None, num=None) -> list:
        """
        通过字典区间返回有序集合的成员
        :return:
            指定区间内的元素列表
        """
        return await self.redis_client.zrangebylex(name, min, max, start=start, num=num)

    async def zrevrangebylex(self, name: str, max: str, min: str, start=None, num=None) -> list:
        """
        返回指定成员区间内的成员，按成员字典倒序排序, 分数必须相同
        :return:
            指定成员范围的元素列表
        """
        return await self.redis_client.zrevrangebylex(name, max, min, start=start, num=num)

    async def zrangebyscore(
            self, name: str, min: Optional[Any], max: Optional[Any],
            start=None, num=None, with_scores=False, score_cast_func=float
    ) -> list:
        """
        通过分数返回有序集合指定区间内的成员

        具有相同分数值的成员按字典序来排列（该属性是有序集提供的，不需要额外的计算）
        默认情况下，区间的取值使用闭区间（小于等于或大于等于），你也可以通过给参数前增加（符号来使用可选的开区间（小于或大于））
        :return:
            指定区间内，带有分数值（可选）的有序集成员的列表
        """
        return await self.redis_client.zrangebyscore(
            name, min, max, start=start, num=num, withscores=with_scores, score_cast_func=score_cast_func
        )

    async def zrank(self, name: str, value: str) -> Optional[Any]:
        """
        返回有序集中指定成员的排名

        其中有序集成员按分数值递增（从小到大）顺序排列
        :return:
            如果成员是有序集 name 的成员，返回 value 的排名。 如果成员不是有序集 name 的成员，返回 nil
        """
        return await self.redis_client.zrank(name, value)

    async def zrem(self, name: str, *values) -> int:
        """
        用于移除有序集中的一个或多个成员，不存在的成员将被忽略

        当 name 存在但不是有序集类型时，返回一个错误
        :return:
            被成功移除的成员的数量，不包括被忽略的成员
        """
        return await self.redis_client.zrem(name, *values)

    async def zremrangebylex(self, name: str, min: str, max: str) -> int:
        """
        移除有序集合中给定的字典区间的所有成员
        :return:
            被成功移除的成员的数量，不包括被忽略的成员
        """
        return await self.redis_client.zremrangebylex(name, min, max)

    async def zremrangebyrank(self, name: str, min: int, max: int) -> int:
        """
        用于移除有序集中，指定排名（rank）区间内的所有成员
        :return:
            被移除成员的数量
        """
        return await self.redis_client.zremrangebyrank(name, min, max)

    async def zremrangebyscore(self, name: str, min: Optional[Any], max: Optional[Any]) -> int:
        """
        移除有序集合中给定的分数区间的所有成员
        :return:
            被移除成员的数量
        """
        return await self.redis_client.zremrangebyscore(name, min, max)

    async def zrevrange(
            self, name: str, start: int, end: int,
            with_scores=False, score_cast_func=float
    ) -> list:
        """
        返回有序集中指定区间内的成员，通过索引，分数从高到低

        其中成员的位置按分数值递减（从大到小）来排列
        具有相同分数值的成员按字典序的逆序（reverse lexicographical order）排列
        除了成员按分数值递减的次序排列这一点外， ZREVRANGE 命令的其他方面和 ZRANGE 命令一样
        :return:
            指定区间内，带有分数值（可选）的有序集成员的列表
        """
        return await self.redis_client.zrevrange(
            name, start, end, withscores=with_scores, score_cast_func=score_cast_func
        )

    async def zrevrangebyscore(
            self, name: str, max: Optional[Any], min: Optional[Any],
            start=None, num=None, with_scores=False, score_cast_func=float
    ) -> list:
        """
        返回有序集中指定分数区间内的成员，分数从高到低排序

        具有相同分数值的成员按字典序的逆序（reverse lexicographical order）排列
        除了成员按分数值递减的次序排列这一点外， ZREVRANGEBYSCORE 命令的其他方面和 ZRANGEBYSCORE 命令一样
        :return:
            指定区间内，带有分数值（可选）的有序集成员的列表
        """
        return await self.redis_client.zrevrangebyscore(
            name, max, min, start=start, num=num, withscores=with_scores, score_cast_func=score_cast_func
        )

    async def zrevrank(self, name: str, value: str) -> Optional[Any]:
        """
        返回有序集合中指定成员的排名，有序集成员按分数值递减（从大到小）排序

        排名以 0 为底，也就是说， 分数值最大的成员排名为 0
        使用 ZRANK 命令可以获得成员按分数值递增（从小到大）排列的排名
        :return:
            如果成员是有序集 name 的成员，返回成员的排名。 如果成员不是有序集 name 的成员，返回 nil
        """
        return await self.redis_client.zrevrank(name, value)

    async def zscore(self, name: str, value: str) -> Optional[Any]:
        """
        返回有序集中，成员的分数值
        :return:
            成员的分数值，以字符串形式表示
        """
        return await self.redis_client.zscore(name, value)

    async def zunionstore(self, dest, keys, aggregate=None):
        """
        计算给定的一个或多个有序集的并集，并存储在新的 dest 中

        默认情况下，结果集中某个成员的分数值是所有给定集下该成员分数值之和
        :return:
            保存到 dest 的结果集的成员数量
        """
        return await self.redis_client.zunionstore(dest, keys, aggregate=aggregate)

    async def zscan(self, name, cursor=0, match=None, count=None, score_cast_func=float):
        """
        迭代有序集合中的元素（包括元素成员和元素分值）
        :return:
            返回的每个元素都是一个有序集合元素，一个有序集合元素由一个成员（member）和一个分值（score）组成
        """
        return await self.redis_client.zscan(
            name, cursor=cursor, match=match, count=count, score_cast_func=score_cast_func
        )


class StreamMixin:
    """
    redis version >= '5.0'
    """

    async def xadd(self, name: str, fields: dict, stream_id='*', max_len=None, approximate=True):
        """
        添加消息到末尾。如果指定的队列不存在，则创建一个队列

        :return
            返回 stream_id
        """
        return await self.redis_client.xadd(name, fields, stream_id=stream_id, max_len=max_len, approximate=approximate)

    async def xlen(self, name: str):
        """
        获取流包含的元素数量，即消息长度
        """
        return await self.redis_client.xlen(name)

    async def xrange(self, name: str, start='-', end='+', count=None):
        """
        获取消息列表，会自动过滤已经删除的消息
        """
        return await self.redis_client.xrange(name, start=start, end=end, count=count)

    async def xrevrange(self, name: str, start='+', end='-', count=None):
        """
        反向获取消息列表，id 从大到小
        """
        return await self.redis_client.xrevrange(name, start=start, end=end, count=count)

    async def xtrim(self, name: str, max_len: int, approximate=True):
        """
        对 stream 进行修剪，限制长度
        """
        return await self.redis_client.xtrim(name, max_len=max_len, approximate=approximate)

    async def xdel(self, name: str, *ids):
        """
        删除消息id对应的消息
        """
        return await self.redis_client.xdel(name, *ids)

    async def xread(self, stream_key: str, stream_id: str, count=None, block=None) -> list:
        """
        以阻塞或非阻塞方式获取消息列表
        :param stream_key: 消息队列名称
        :param stream_id: 读取的起始位置索引
        :param count: 数量
        :param block: 阻塞毫秒数，没有设置就是非阻塞模式
        :return:
            指定条件下的消息列表
        """
        return await self.redis_client.xread(count=count, block=block, **{stream_key: stream_id})

    async def first_stream_record(self, name: str) -> list:
        """
        获取 stream 中第一条数据
        """
        record = await self.redis_client.xrange(name, count=1)
        if not record:
            return []
        return record[0]

    async def last_stream_record(self, name: str) -> list:
        """
        获取 stream 中最后一条数据
        """
        record = await self.redis_client.xrevrange(name, count=1)
        if not record:
            return []
        return record[0]


class RedisClient(StringMixin, ListMixin, SetMixin, HashMixin, ZSetMixin, StreamMixin):
    """
    website http://www.redis.cn/commands.html
    """

    def __init__(self, host='127.0.0.1', port=6379, db=0) -> None:
        self.redis_client = StrictRedis(host=host, port=port, db=db)

    async def flushdb(self) -> bool:
        """
        清空连接的数据库
        """
        return await self.redis_client.flushdb()

    async def keys(self, key: str) -> list:
        """
        查找所有符合给定模式(pattern)的 key
        """
        return await self.redis_client.keys(key)

    async def expire(self, name: str, time: int) -> bool:
        """
        为给定 key 设置过期时间，以秒计
        """
        return await self.redis_client.expire(name, time)

    async def delete(self, key: str) -> int:
        """
        key 存在时删除 key
        """
        return await self.redis_client.delete(key)
