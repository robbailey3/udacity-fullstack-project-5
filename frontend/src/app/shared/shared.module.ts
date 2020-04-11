import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CardComponent } from './components/card/card.component';
import { IntersectionDirective } from './directives/intersection.directive';

@NgModule({
  declarations: [CardComponent, IntersectionDirective],
  exports: [CardComponent, IntersectionDirective],
  imports: [CommonModule]
})
export class SharedModule {}
