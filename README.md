Authenticating with SASL PLAIN

### Requirements
+ Python installed
+ `pip` and `virtualenv` installed (or `pip3`)

### Start

```bash
virtualenv env
source env/bin/activate
pip install confluent-kafka
````

### Usage
Assuming you have a Kafka broker running on `localhost:9092` and a topic called `test`, an user called `admin` with password `admin` is allowed to read, write topic.
+ Run consumer:
    ```python
    ./env/bin/python consumer.py
    ```
+ Run producer
    ```python
    ./env/bin/python producer.py
    ```