# imgae with basic linux env plus latest python version
FROM python 

# new dir to contain microservice code
RUN mkdir /service
# copy required source code to microservice dir
COPY protobufs/ /service/protobufs/
COPY recommendations/ /service/recommendations/
# set working directory
WORKDIR /service/recommendations
# install dependencies
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/recommendations.proto

# define port of microservice
EXPOSE 50051
# run microservice
ENTRYPOINT [ "python", "recommendations.py" ]
# build: docker build . -f recommendations/Dockerfile -t recommendations
# run a container: docker run -p 127.0.0.1:50051:50051/tcp recommendations