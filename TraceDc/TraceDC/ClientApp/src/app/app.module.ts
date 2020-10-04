import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";

import { AppRoutingModule } from "./app-routing.module";
import { AppComponent } from "./app.component";
import { LineChartComponent } from "./line-chart/line-chart.component";

import { ChartsModule } from "ng2-charts";

@NgModule({
  declarations: [
    AppComponent,
    LineChartComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ChartsModule
  ],
  providers: [
    { provide: "BASE_URL", useFactory: getBaseUrl}
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
}

export function getBaseUrl() {
  return document.getElementsByTagName("base")[0].href;
}
