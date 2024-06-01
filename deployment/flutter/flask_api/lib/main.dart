import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  final FocusNode _focusNode = FocusNode();
  final TextEditingController weekCon = TextEditingController(text: '2');
  final TextEditingController homeBetCon = TextEditingController(text: '1.2');
  final TextEditingController awayBetCon = TextEditingController(text: '1.2');
  final TextEditingController drawBetCon = TextEditingController(text: '1.2');
  final TextEditingController altBetCon = TextEditingController(text: '1.2');
  final TextEditingController ustBetCon = TextEditingController(text: '1.2');
  final TextEditingController homePointCon = TextEditingController(text: '99');
  final TextEditingController awayPointCon = TextEditingController(text: '33');

  String? homeTeam;
  String? awayTeam;
  String? refree;

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: GestureDetector(
        onTap: () {
          if (_focusNode.hasFocus) {
            _focusNode.unfocus();
          }
        },
        child: Scaffold(
          resizeToAvoidBottomInset: false,
          appBar: AppBar(
            backgroundColor: Colors.red,
            title: const Text(
              'Super Leauge Predict Total Goal',
              style:
                  TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
            ),
          ),
          body: Center(
            child: Padding(
              padding: const EdgeInsets.all(8.0),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Column(
                    children: [
                      InputField(label: 'Week', controller: weekCon),
                      InputDrop(
                        label: 'Refree',
                        isList: false,
                        onChanged: (value) {
                          setState(() {
                            refree = value;
                          });
                        },
                      ),
                      InputDrop(
                        label: 'Home Team',
                        isList: true,
                        onChanged: (value) {
                          setState(() {
                            homeTeam = value;
                          });
                        },
                      ),
                      InputDrop(
                        label: 'Away Team',
                        isList: true,
                        onChanged: (value) {
                          setState(() {
                            awayTeam = value;
                          });
                        },
                      ),
                      _buildInputRow([
                        'Home Bet',
                        'Draw Bet',
                        'Away Bet',
                      ], [
                        homeBetCon,
                        drawBetCon,
                        awayBetCon,
                      ]),
                      _buildInputRow([
                        'Alt Bet',
                        'Ust Bet',
                      ], [
                        altBetCon,
                        ustBetCon,
                      ]),
                      _buildInputRow([
                        'Home Point',
                        'Away Point',
                      ], [
                        homePointCon,
                        awayPointCon,
                      ]),
                    ],
                  ),
                  FutureBuilder(
                    future: postData(
                      int.parse(weekCon.text),
                      double.parse(homeBetCon.text),
                      double.parse(drawBetCon.text),
                      double.parse(awayBetCon.text),
                      double.parse(altBetCon.text),
                      double.parse(ustBetCon.text),
                      int.parse(homePointCon.text),
                      int.parse(awayPointCon.text),
                      homeTeam,
                      awayTeam,
                      refree,
                    ),
                    builder: (context, snapshot) {
                      if (snapshot.hasData) {
                        Map? data = snapshot.data;
                        return Column(
                          mainAxisAlignment: MainAxisAlignment.start,
                          children: [
                            Text(
                              'Predicted total number of goals',
                              style: TextStyle(
                                fontFamily: GoogleFonts.aBeeZee().fontFamily,
                                color: Colors.red,
                              ),
                            ),
                            Text(
                              data!['response'],
                              textAlign: TextAlign.center,
                              style: TextStyle(
                                fontSize: 40,
                                fontWeight: FontWeight.bold,
                                fontFamily: GoogleFonts.aBeeZee().fontFamily,
                                color: Colors.red,
                              ),
                            ),
                          ],
                        );
                      } else {
                        return Text(
                          'PLEASE ENTER ALL INFORMATION\nOR\nSTART API.PY PROJECT FIRST',
                          textAlign: TextAlign.center,
                          style: TextStyle(
                            fontFamily: GoogleFonts.aBeeZee().fontFamily,
                            color: Colors.red,
                          ),
                        );
                      }
                    },
                  ),
                  GestureDetector(
                    onTap: () {
                      setState(() {});
                    },
                    child: Container(
                      height: 50,
                      width: double.infinity,
                      decoration: BoxDecoration(
                          color: Colors.red,
                          borderRadius: BorderRadius.circular(8)),
                      child: const Center(
                          child: Text(
                        'PREDICT',
                        style: TextStyle(
                            color: Colors.white, fontWeight: FontWeight.bold),
                      )),
                    ),
                  ),
                  const SizedBox()
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }

  Future<Map<String, dynamic>> postData(
      int week,
      double homeBet,
      double drawBet,
      double awayBet,
      double altBet,
      double ustBet,
      int homePoint,
      int awayPoint,
      String? homeTeam,
      String? awayTeam,
      String? refree) async {
    var url = Uri.parse('http://127.0.0.1:5000/');
    var body = {
      'input': jsonEncode({
        'week': week,
        'home': homeTeam,
        'away': awayTeam,
        'referee': refree,
        'home_bets': homeBet,
        'away_bets': awayBet,
        'draw_bets': drawBet,
        'alt_bet': altBet,
        'ust_bet': ustBet,
        'home_point': homePoint,
        'away_point': awayPoint,
      }),
    };
    var response = await http.post(url, body: body);
    return jsonDecode(response.body);
  }

  Widget _buildInputRow(
      List<String> labels, List<TextEditingController> controllers) {
    return Row(
      children: List.generate(labels.length, (index) {
        return Expanded(
          child: Padding(
            padding: const EdgeInsets.only(right: 8.0),
            child: InputField(
              label: labels[index],
              controller: controllers[index],
            ),
          ),
        );
      }),
    );
  }
}

class InputField extends StatelessWidget {
  final String label;
  final TextEditingController controller;

  const InputField({super.key, required this.label, required this.controller});

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(label),
        Container(
          decoration: BoxDecoration(
            border: Border.all(color: Colors.black.withOpacity(0.2)),
            borderRadius: BorderRadius.circular(8),
          ),
          child: Padding(
            padding: const EdgeInsets.only(left: 8.0),
            child: TextField(
              keyboardType:
                  const TextInputType.numberWithOptions(decimal: true),
              decoration: const InputDecoration(border: InputBorder.none),
              controller: controller,
            ),
          ),
        ),
      ],
    );
  }
}

class InputDrop extends StatefulWidget {
  final String label;
  final bool isList;
  final ValueChanged<String?> onChanged;

  const InputDrop(
      {Key? key,
      required this.label,
      this.isList = true,
      required this.onChanged})
      : super(key: key);

  @override
  _InputDropState createState() => _InputDropState();
}

class _InputDropState extends State<InputDrop> {
  String? selectedValue;
  static const List<String> teams = [
    'Trabzonspor',
    'Kasımpaşa',
    'Konyaspor',
    'Pendikspor',
    'Kayserispor',
    'Sivasspor',
    'Adana',
    'Fenerbahce',
    'Karagumruk',
    'Alanya',
    'Istanbulspor',
    'Antalyaspor',
    'Rize',
    'Galatasaray',
    'Hatayspor',
    'Basaksehir',
    'Beşiktaş',
    'Gaziantep',
    'Ankaragücü',
    'Samsunspor'
  ];

  static const List<String> refrees = [
    'Zorbay Kucuk',
    'Bahattin Simsek',
    'Burak Pakkan',
    'Cagdas Altay',
    'Halil Umut Meler',
    'Murat Erdogan',
    'Ümit Ozturk',
    'Abdulkadir Bitigen',
    'Rare',
    'Tugay Numanoglu',
    'Ali Sansalan',
    'Atilla Karaoğlan',
    'Mert Guzenge',
    'Burak Seker',
    'Kadir Saglam',
    'Arda Kardesler',
    'Cihan Aydin',
    'Volkan Bayarslan',
    'Turgut Doman',
    'Direnç Tosunoğlu',
    'Emre Kargin'
  ];

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(widget.label),
        Container(
          decoration: BoxDecoration(
            border: Border.all(color: Colors.black.withOpacity(0.2)),
            borderRadius: BorderRadius.circular(8),
          ),
          child: Padding(
            padding: const EdgeInsets.only(left: 8.0),
            child: DropdownButton<String>(
              value: selectedValue,
              isExpanded: true,
              underline: const SizedBox(),
              items: (widget.isList ? teams : refrees).map((String value) {
                return DropdownMenuItem<String>(
                  value: value,
                  child: Text(value),
                );
              }).toList(),
              onChanged: (String? newValue) {
                setState(() {
                  selectedValue = newValue;
                });
                widget.onChanged(newValue);
              },
            ),
          ),
        ),
      ],
    );
  }
}
