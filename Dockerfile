FROM slave4.wizeye.com.cn:5000/ubuntu-python
COPY duplicate.py /home/duplicate.py
CMD python /home/duplicate.py