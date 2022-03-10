import os

"""
ENV SOURCE_TYPE standalone
ENV SOURCE_ADDRESS 127.0.0.1:20441
ENV SOURCE_PASSWORD_RAW 123456
ENV TARGET_TYPE standalone
ENV TARGET_ADDRESS 127.0.0.1:6379
ENV TARGET_PASSWORD_RAW 123456
ENV TARGET_DB -1

ENV KEY_EXISTS none
ENV FILTER_DB_WHITELIST -1
ENV FILTER_DB_BLACKLIST -1
ENV FILTER_KEY_WHITELIST -1
ENV FILTER_KEY_BLACKLIST -1
ENV LOG_LEVEL info

ENV BIG_KEY_THRESHOLD 524288000

ENV TYPE sync
"""

SOURCE_TYPE = os.getenv('SOURCE_TYPE')
SOURCE_ADDRESS = os.getenv('SOURCE_ADDRESS')
SOURCE_PASSWORD_RAW = os.getenv('SOURCE_PASSWORD_RAW')
TARGET_TYPE = os.getenv('TARGET_TYPE')
TARGET_ADDRESS = os.getenv('TARGET_ADDRESS')
TARGET_PASSWORD_RAW = os.getenv('TARGET_PASSWORD_RAW')
TARGET_DB = os.getenv('TARGET_DB')
KEY_EXISTS = os.getenv('KEY_EXISTS')
FILTER_DB_WHITELIST = os.getenv('FILTER_DB_WHITELIST')
FILTER_DB_BLACKLIST = os.getenv('FILTER_DB_BLACKLIST')
FILTER_KEY_WHITELIST = os.getenv('FILTER_KEY_WHITELIST')
FILTER_KEY_BLACKLIST = os.getenv('FILTER_KEY_BLACKLIST')
LOG_LEVEL = os.getenv('LOG_LEVEL')
BIG_KEY_THRESHOLD = os.getenv('BIG_KEY_THRESHOLD')
TYPE = os.getenv('TYPE')

redis_shake_conf = '/usr/local/app/redis-shake.conf'
with open(redis_shake_conf, 'r') as f:
    lines = f.readlines()
new_lines = []
for line in lines:
    if line.strip().startswith('source.type = standalone') and SOURCE_TYPE != 'standalone':
        new_line = 'source.type = %s' % SOURCE_TYPE
        new_lines.append(new_line)
        print(new_line)
        continue
    if line.strip().startswith('source.address = 127.0.0.1:20441') and SOURCE_ADDRESS != '127.0.0.1:20441':
        new_line = 'source.address = %s' % SOURCE_ADDRESS
        new_lines.append(new_line)
        print(new_line)
        continue
    if line.strip().startswith('source.password_raw =') and SOURCE_PASSWORD_RAW != '123456':
        new_line = 'source.password_raw = %s' % SOURCE_PASSWORD_RAW
        new_lines.append(new_line)
        print(new_line)
        continue
    if line.strip().startswith('target.type = standalone') and TARGET_TYPE != 'standalone':
        new_line = 'target.type = %s' % TARGET_TYPE
        new_lines.append(new_line)
        print(new_line)
        continue
    if line.strip().startswith('target.address = 127.0.0.1:6379') and TARGET_ADDRESS != '127.0.0.1:6379':
        new_line = 'target.address = %s' % TARGET_ADDRESS
        new_lines.append(new_line)
        print(new_line)
        continue
    if line.strip().startswith('target.password_raw =') and TARGET_PASSWORD_RAW != '123456':
        new_line = 'target.password_raw = %s' % TARGET_PASSWORD_RAW
        new_lines.append(new_line)
        print(new_line)
        continue
    if line.strip().startswith('target.db = -1') and TARGET_DB != '-1':
        new_line = 'target.db = %s' % TARGET_DB
        new_lines.append(new_line)
        print(new_line)
        continue
    if line.strip().startswith('key_exists = none') and KEY_EXISTS != 'none':
        new_line = 'key_exists = %s' % KEY_EXISTS
        new_lines.append(new_line)
        print(new_line)
        continue
    if line.strip().startswith('filter.db.whitelist =') and FILTER_DB_WHITELIST != '-1':
        new_line = 'filter.db.whitelist = %s' % FILTER_DB_WHITELIST
        new_lines.append(new_line)
        print(new_line)
        continue
    if line.strip().startswith('filter.db.blacklist =') and FILTER_DB_BLACKLIST != '-1':
        new_line = 'filter.db.blacklist = %s' % FILTER_DB_BLACKLIST
        new_lines.append(new_line)
        print(new_line)
        continue
    if line.strip().startswith('filter.key.whitelist =') and FILTER_KEY_WHITELIST != '-1':
        new_line = 'filter.key.whitelist = %s' % FILTER_KEY_WHITELIST
        new_lines.append(new_line)
        print(new_line)
        continue
    if line.strip().startswith('filter.key.blacklist =') and FILTER_KEY_BLACKLIST != '-1':
        new_line = 'filter.key.blacklist = %s' % FILTER_KEY_BLACKLIST
        new_lines.append(new_line)
        print(new_line)
        continue
    if line.strip().startswith('log.level = info') and LOG_LEVEL != 'info':
        new_line = 'log.level = %s' % LOG_LEVEL
        new_lines.append(new_line)
        print(new_line)
        continue
    if line.strip().startswith('big_key_threshold = 524288000') and BIG_KEY_THRESHOLD != '524288000':
        new_line = 'big_key_threshold = %s' % BIG_KEY_THRESHOLD
        new_lines.append(new_line)
        print(new_line)
        continue
    new_lines.append(line.strip())
with open(redis_shake_conf, 'w') as f:
    f.write('\n'.join(new_lines))

os.system('/usr/local/app/redis-shake -type=%s -conf=/usr/local/app/redis-shake.conf' % TYPE)

