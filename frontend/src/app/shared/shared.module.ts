import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CardComponent } from './components/card/card.component';
import { IntersectionDirective } from './directives/intersection.directive';
import { CacheModule } from './cache/cache.module';
import { SafePipe } from './pipes/safe.pipe';
import { NotificationsModule } from './notifications/notifications.module';

@NgModule({
  declarations: [CardComponent, IntersectionDirective, SafePipe],
  exports: [
    CardComponent,
    IntersectionDirective,
    SafePipe,
    NotificationsModule
  ],
  imports: [CommonModule, CacheModule, NotificationsModule]
})
export class SharedModule {}
