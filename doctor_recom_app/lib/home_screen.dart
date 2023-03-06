import 'dart:developer';

import 'package:dio/dio.dart';
import 'package:flutter/material.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  TextEditingController symptomsController = TextEditingController();

  Dio dio = Dio();
  static const endpoint = "http://0.0.0.0:8000/api/recommend-doctor";

  Future<List> getData(String symptoms) async {
    final response = await dio.post(endpoint, data: {
      "symptoms": symptoms,
    });
    log(response.data['data'].toString(), name: 'respond');
    return response.data['data'];
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Doctor Recommandation System"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(15.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          children: [
            const SizedBox(height: 10),
            const Text("Please enter symptoms"),
            const SizedBox(height: 10),
            TextField(
              controller: symptomsController,
              decoration: const InputDecoration(
                labelText: "symptoms",
              ),
              minLines: 1,
              maxLines: 4,
              onEditingComplete: () {
                getData(symptomsController.text);
                setState(() {});
              },
              onSubmitted: (_) {
                getData(symptomsController.text);
                setState(() {});
              },
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                getData(symptomsController.text);
                setState(() {});
              },
              child: const Text("Generate Recomandation"),
            ),
            const SizedBox(height: 10),
            const Text(
              "Recommanded Diseases",
              style: TextStyle(
                fontWeight: FontWeight.bold,
                fontSize: 20,
              ),
            ),
            const SizedBox(height: 20),
            FutureBuilder(
              future: getData(symptomsController.text),
              builder: (context, AsyncSnapshot<List> snapshot) {
                if (snapshot.connectionState == ConnectionState.waiting) {
                  return const CircularProgressIndicator();
                } else if (snapshot.connectionState == ConnectionState.done) {
                  if (snapshot.hasError) {
                    return const Text('Data Not Found');
                  } else if (snapshot.hasData) {
                    return ListView.builder(
                      shrinkWrap: true,
                      itemCount: snapshot.data?.length ?? 0,
                      itemBuilder: (context, index) {
                        return Card(
                          color: Colors.blue.withOpacity(0.6),
                          child: SizedBox(
                            height: 30,
                            child: Center(
                              child: Text(snapshot.data?[index] ?? ''),
                            ),
                          ),
                        );
                      },
                    );
                  } else {
                    return const Text('Empty data');
                  }
                } else {
                  return Text('State: ${snapshot.connectionState}');
                }
              },
            ),
          ],
        ),
      ),
    );
  }
}
