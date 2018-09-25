# Audio Processing in Python

This is a very simple client-server application for capturing and processing the audio signals. This is first version of the application which does not include the processing part.

## Client side
Client side application is responsible for capturing the audio signal and transmitting these signals to the server.

## Server side
Server is responsible to process recevied audio signal and display the results. Currently, this server is single threaded which only support one client. This functionality can be easily extended for multiple clients by embedding multithreading capabilities. Right now, server code is using a simple threshold value to check existence of voice. It then display when there is silence and when there is voice activity.
