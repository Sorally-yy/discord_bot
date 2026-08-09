# 両方をバックグラウンドで起動しつつ監視

python healthcheck_server.py &
python app/main.py

# discord_bot.py を終了させたらコンテナも終了
