"""总逻辑：
1.frontend里的user_main调用logic中的view
2.logic里的view调用db中的sql_api(去数据库查数据）
3.sql_api再调用config里settings的DATABASE（依赖验证）
"""