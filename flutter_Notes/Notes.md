# Flutter | Networking      
## Fetch Data From The Internet
Before you can use networking in Flutter need to config this in AndroidManifest.xml
~~~xml
<manifest xmlns:android...>
 ...
 <uses-permission android:name="android.permission.INTERNET" />
 <application ...
</manifest>
~~~    
Dart and flutter also uses http packages   
but must avoid ***dart:io*** and ***dart:html*** -> since they are platform dependent   
   
1. Add the Http Package   
~~~
flutter pub add http
~~~   
~~~
import 'package:http/http.dart' as http;
~~~   
~~~
<!-- Required to fetch data from the internet. -->
<uses-permission android:name="android.permission.INTERNET" />~~~     

2. Make network request   
~~~
Future<http.Response> fetchAlbum() {
  return http.get(Uri.parse('https://jsonplaceholder.typicode.com/albums/1'));
}
~~~
3 .Convert a response to a custom dart Obj
Need to convert it to a json map that takes in String and dynamic as args

4 .Fetch and display The Data   
 
## Communicate in Websockets   
1. Connect to the Websocket Server   
~~~
final channel = WebSocketChannel.connect(
  Uri.parse('wss://echo.websocket.events'),
);
~~~   
2. Listen for Messages   
~~~
StreamBuilder(
  stream: channel.stream,
  builder: (context, snapshot) {
    return Text(snapshot.hasData ? '${snapshot.data}' : '');
  },
)
~~~   
3. Also Remember to update the .yaml file
~~~
dependencies:
  web_socket_channel: ^3.0.1
~~~
