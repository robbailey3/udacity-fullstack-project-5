import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ActorsRootComponent } from './actors-root/actors-root.component';
import { ActorsListComponent } from './actors-list/actors-list.component';
import { AuthGuard } from '../auth/auth.guard';
import { ActorProfileComponent } from './actor-profile/actor-profile.component';
import { ActorEditComponent } from './actor-edit/actor-edit.component';
import { ActorCreateComponent } from './actor-create/actor-create.component';

const routes: Routes = [
  {
    path: 'actors',
    component: ActorsRootComponent,
    canActivate: [AuthGuard],
    children: [
      { path: '', pathMatch: 'full', component: ActorsListComponent },
      { path: 'create', component: ActorCreateComponent },
      { path: ':id', component: ActorProfileComponent },
      { path: ':id/edit', component: ActorEditComponent }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ActorsRoutingModule {}
