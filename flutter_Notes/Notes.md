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
# Data Persistance using SQFLite    
1. Add Dependencies   
~~~
flutter pub add sqflite path run on terminal

imports *

import 'dart:async';

import 'package:flutter/widgets.dart';
import 'package:path/path.dart';
import 'package:sqflite/sqflite.dart';

~~~   
2. Create a Model   
The model you want to use in your db , i.e if    
Person , then person must have attributes   
declare a model   
~~~
class Abonigle{
final School String ...

const Abongile({required this.School}) -> constructor
}

~~~
3. Open a DB  
~~~flutter
void main() async {
  // Avoid errors caused by flutter upgrade.
  // Importing 'package:flutter/widgets.dart' is required.
  WidgetsFlutterBinding.ensureInitialized();
  // Open the database and store the reference.
  final database = openDatabase(
    // Set the path to the database. Note: Using the `join` function from the
    // `path` package is best practice to ensure the path is correctly
    // constructed for each platform.
    join(await getDatabasesPath(), 'doggie_database.db'),
~~~     
4. Create a Table in the db   
~~~flutter
Complete open and create a table code
void main() async {
  // Avoid errors caused by flutter upgrade.
  // Importing 'package:flutter/widgets.dart' is required.
  WidgetsFlutterBinding.ensureInitialized();
  // Open the database and store the reference.
  final database = openDatabase(
    // Set the path to the database. Note: Using the `join` function from the
    // `path` package is best practice to ensure the path is correctly
    // constructed for each platform.
    join(await getDatabasesPath(), 'doggie_database.db'),
    // When the database is first created, create a table to store dogs.
    onCreate: (db, version) {
      // Run the CREATE TABLE statement on the database.
      return db.execute(
        'CREATE TABLE dogs(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)',
      );
    },
    // Set the version. This executes the onCreate function and provides a
    // path to perform database upgrades and downgrades.
    version: 1,
  );
~~~






