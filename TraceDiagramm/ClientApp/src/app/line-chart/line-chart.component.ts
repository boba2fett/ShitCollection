import { Component, OnInit, Inject } from "@angular/core";
import { ChartDataSets } from "chart.js";
import { Color } from "ng2-charts";
import { DiagramData, Category, Pair} from "../diagram-data";
import { HttpClient } from "@angular/common/http";

@Component({
  selector: "app-line-chart",
  templateUrl: "./line-chart.component.html",
  styleUrls: ["./line-chart.component.css"],
})
export class LineChartComponent implements OnInit {
  bugs: { x: Date; y: number }[] = null;
  bugsInProgress: { x: Date; y: number }[];
  diaData: DiagramData;


  constructor(public http: HttpClient, @Inject("BASE_URL") public baseUrl: string) {}

  lineChartData: ChartDataSets[];
  error = null;

  lineChartOptions = {
    scales: {
      xAxes: [
        {
          type: "time",
          time: {
            unit: "day",
          },
        },
      ],
      yAxes: [
        {
          ticks: {
            beginAtZero: true
          }
        }
      ]
    },
    responsive: true,
  };

  lineChartColors: Color[] = [
  ];

  lineChartLegend = true;
  lineChartPlugins = [];
  lineChartType = "line";

  getData(): void {
    this.http.get<DiagramData>(this.baseUrl + "api/data").subscribe(result => {
        this.diaData = result;
      },
      error => {
        console.error(error);
        this.error = "An Error occurred while loading the data from the server";
      },
      () => {
        this.lineChartData = this.diaData.categories;

      }
    );



    console.log(this.diaData);
  }

  ngOnInit() {
    this.getData();

  }
}
