# -*- coding: utf-8 -*-

from methods.redis import RedisClient


async def test_string(redis_client: RedisClient, name="test_string") -> None:
    print('-' * 16, 'string 语法测试', '-' * 16)
    print(await redis_client.set(name, 'string'))
    print(await redis_client.get(name))
    print(await redis_client.strlen(name))
    print(await redis_client.delete(name))


async def test_list(redis_client: RedisClient, name='test_list') -> None:
    print('-' * 16, 'list 语法测试', '-' * 16)
    print(await redis_client.lpush(name, '1'))
    print(await redis_client.llen(name))
    print(await redis_client.lpush(name, '2'))
    print(await redis_client.delete(name))


async def test_stream(redis_client: RedisClient, name='test_stream') -> None:
    from datetime import datetime
    date_str = datetime.now().strftime('%Y%m%d')

    print('-' * 16, 'stream 语法测试', '-' * 16)
    print(await redis_client.xadd(name, {'name': '247gzs'}, stream_id=f"{date_str}-1"))
    print(await redis_client.xadd(name, {'name': '247gzs'}, stream_id=f"{date_str}-2"))
    print(await redis_client.xread(stream_key=name, stream_id=f'{date_str}-0', count=10))
    print(await redis_client.first_stream_record(name))
    print(await redis_client.last_stream_record(name))
    print(await redis_client.xdel(name, *[f'{date_str}-1']))
    # print(await redis_client.delete(name))


async def test_hash(redis_client: RedisClient, name='test_hash') -> None:
    print('-' * 16, 'hash 语法测试', '-' * 16)
    print(await redis_client.hset(name, 'google', 'www.google.com'))
    print(await redis_client.hget(name, 'google'))
    print(await redis_client.hvals(name))
    print(await redis_client.hlen(name))
    print(await redis_client.hdel(name, *['baidu', 'sina']))
    print(await redis_client.delete(name))


async def test_set(redis_client: RedisClient, name='test_set') -> None:
    print('-' * 16, 'set 语法测试', '-' * 16)
    print(await redis_client.sadd(name, *['a', 'b', 'c', 'd']))
    print(await redis_client.scard(name))
    print(await redis_client.sadd('test_set_2', *['b', 'c', 'd']))
    print(await redis_client.sdiff([name, 'test_set_2']))
    print(await redis_client.smembers(name))
    print(await redis_client.sscan(name, count=2))
    print(await redis_client.delete('test_set_2'))
    print(await redis_client.delete(name))


async def test_sorted_set(redis_client: RedisClient, name='test_sorted_set') -> None:
    print('-' * 16, 'sorted set 语法测试', '-' * 16)
    print(await redis_client.zadd(name, **{'a': 10, 'b': 30, 'c': 20}))
    print(await redis_client.zaddoption(name, option='XX', **{'a': 100, 'd': 50}))
    print(await redis_client.zaddoption(name, option='NX CH', **{'a': 10, 'd': 50}))
    print(await redis_client.zcard(name))
    print(await redis_client.zrange(name, start=0, end=10))
    print(await redis_client.zrangebylex(name, '-', '+'))
    print(await redis_client.zrangebylex(name, '[aaa', '+'))
    print(await redis_client.zrangebylex(name, '-', '(c'))
    print(await redis_client.zrangebyscore(name, '-inf', '+inf', with_scores=True, score_cast_func=int))
    print(await redis_client.zrank(name, 'e'))
    print(await redis_client.zrank(name, 'a'))
    print(await redis_client.zrem(name, 'a'))
    print(await redis_client.zrem(name, 'e'))
    print(await redis_client.zrevrange(name, start=0, end=10, with_scores=True, score_cast_func=int))
    print(await redis_client.zrevrangebyscore(name, max=100, min=0, with_scores=True, score_cast_func=int))
    print(await redis_client.zrevrank(name, 'c'))
    print(await redis_client.zrevrank(name, 'e'))
    print(await redis_client.zscore(name, 'c'))
    print(await redis_client.zscore(name, 'e'))
    print(await redis_client.delete(name))


async def main():
    redis_client = RedisClient()
    await test_string(redis_client)
    await test_list(redis_client)
    await test_stream(redis_client)
    await test_hash(redis_client)
    await test_set(redis_client)
    await test_sorted_set(redis_client)


if __name__ == '__main__':
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
