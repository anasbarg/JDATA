import {
  MatToolbarModule,
  MatTabsModule,
  MatCardModule
} from "@angular/material";
import { NgModule } from "@angular/core";
@NgModule({
  imports: [MatToolbarModule, MatTabsModule, MatCardModule],
  exports: [MatToolbarModule, MatTabsModule, MatCardModule]
})
export class MaterialModule {}
