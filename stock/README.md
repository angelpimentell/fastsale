```sh
pip install -r requirements.txt
```

```sh
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

```sh
python app.py
```