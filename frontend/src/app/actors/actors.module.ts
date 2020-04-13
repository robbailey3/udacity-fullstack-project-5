import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActorsRootComponent } from './actors-root/actors-root.component';
import { ActorsListComponent } from './actors-list/actors-list.component';
import { ActorEditComponent } from './actor-edit/actor-edit.component';
import { ActorCreateComponent } from './actor-create/actor-create.component';
import { ActorProfileComponent } from './actor-profile/actor-profile.component';
import { ActorsRoutingModule } from './actors-routing.module';
import { SharedModule } from '../shared/shared.module';
import { RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    ActorsRootComponent,
    ActorsListComponent,
    ActorEditComponent,
    ActorCreateComponent,
    ActorProfileComponent
  ],
  imports: [
    CommonModule,
    ActorsRoutingModule,
    SharedModule,
    RouterModule,
    FormsModule
  ]
})
export class ActorsModule {}
