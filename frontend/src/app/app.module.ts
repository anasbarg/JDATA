// Modules
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { MaterialModule } from './material';
import { AppRoutingModule } from './app-routing.module';
import { FormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { ChartsModule } from 'ng2-charts';
// Components
import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { ContentComponent } from './content/content.component';
import { ChartCardComponent } from './chart-card/chart-card.component';
import { ChartControllersComponent } from './chart-controllers/chart-controllers.component';
import { SliderComponent } from './slider/slider.component';
import { DropdownControllerComponent } from './dropdown-controller/dropdown-controller.component';
import { ChartComponent } from './chart/chart.component';

@NgModule({
    declarations: [
        AppComponent,
        NavbarComponent,
        ContentComponent,
        ChartCardComponent,
        ChartControllersComponent,
        SliderComponent,
        DropdownControllerComponent,
        ChartComponent,
    ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        BrowserAnimationsModule,
        MaterialModule,
        FormsModule,
        HttpClientModule,
        CommonModule,
        ChartsModule,
    ],
    bootstrap: [AppComponent],
})
export class AppModule {}
