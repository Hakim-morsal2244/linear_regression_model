import 'package:flutter/material.dart';
import 'services/prediction_service.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: PredictionPage(),
    );
  }
}

class PredictionPage extends StatefulWidget {
  @override
  _PredictionPageState createState() => _PredictionPageState();
}

class _PredictionPageState extends State<PredictionPage> {
  final _hoursController = TextEditingController();
  final _attendanceController = TextEditingController();
  final _previousController = TextEditingController();
  final PredictionService _service = PredictionService();
  String? _result;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Exam Score Predictor")),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          children: [
            TextField(controller: _hoursController, decoration: InputDecoration(labelText: "Hours Studied"), keyboardType: TextInputType.number),
            TextField(controller: _attendanceController, decoration: InputDecoration(labelText: "Attendance (%)"), keyboardType: TextInputType.number),
            TextField(controller: _previousController, decoration: InputDecoration(labelText: "Previous Scores"), keyboardType: TextInputType.number),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () async {
                final prediction = await _service.getPrediction(
                  int.parse(_hoursController.text),
                  int.parse(_attendanceController.text),
                  int.parse(_previousController.text),
                );
                setState(() => _result = prediction != null ? "Predicted Exam Score: $prediction" : "Error");
              },
              child: Text("Predict"),
            ),
            SizedBox(height: 20),
            Text(_result ?? ""),
          ],
        ),
      ),
    );
  }
}