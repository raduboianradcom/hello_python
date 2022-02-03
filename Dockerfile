FROM python:onbuild
COPY requirements.txt .
ENV PORT 5003
EXPOSE 5003
ENTRYPOINT ["python"]
CMD ["main.py"]
