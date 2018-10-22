// Modules
import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";
import { MaterialModule } from "./material";
import { AppRoutingModule } from "./app-routing.module";
import { FormsModule } from "@angular/forms";
import { BrowserAnimationsModule } from "@angular/platform-browser/animations";
import { HttpClientModule } from "@angular/common/http";

// Components
import { AppComponent } from "./app.component";
import { NavbarComponent } from "./navbar/navbar.component";
import { ContentComponent } from "./content/content.component";

// Services
import { ChartConfigService } from "./services/chart-config.service";
import { ChartCardComponent } from './chart-card/chart-card.component';

@NgModule({
  declarations: [AppComponent, NavbarComponent, ContentComponent, ChartCardComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MaterialModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [ChartConfigService],
  bootstrap: [AppComponent]
})
export class AppModule {}
