FROM postgres:12.20

# ロケールの設定
RUN localedef -i ja_JP -c -f UTF-8 -A /usr/share/locale/locale.alias ja_JP.UTF-8
ENV LANG ja_JP.utf8

# タイムゾーンの設定
ENV TZ Asia/Tokyo
# FROM postgres:12.20

# ENV TZ Asia/Tokyo

# ENV LANG ja_JP.UTF-8
# ENV LANGUAGE ja_JP:ja
# ENV LC_ALL ja_JP.UTF-8