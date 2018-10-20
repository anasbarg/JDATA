import { MatToolbarModule, MatTabsModule } from "@angular/material";
import { NgModule } from "@angular/core";
@NgModule({
  imports: [MatToolbarModule, MatTabsModule],
  exports: [MatToolbarModule, MatTabsModule]
})
export class MaterialModule {}
