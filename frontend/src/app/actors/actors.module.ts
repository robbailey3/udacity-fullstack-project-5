import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActorsRootComponent } from './actors-root/actors-root.component';
import { ActorsListComponent } from './actors-list/actors-list.component';
import { ActorsProfileComponent } from './actors-profile/actors-profile.component';



@NgModule({
  declarations: [ActorsRootComponent, ActorsListComponent, ActorsProfileComponent],
  imports: [
    CommonModule
  ]
})
export class ActorsModule { }
