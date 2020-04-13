import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { MoviesRootComponent } from './movies-root/movies-root.component';
import { MoviesListComponent } from './movies-list/movies-list.component';
import { AuthGuard } from '../auth/auth.guard';
import { MoviesDetailComponent } from './movies-detail/movies-detail.component';
import { MovieEditComponent } from './movie-edit/movie-edit.component';
import { MovieCreateComponent } from './movie-create/movie-create.component';

const routes: Routes = [
  {
    path: 'movies',
    component: MoviesRootComponent,
    canActivate: [AuthGuard],
    children: [
      { path: '', pathMatch: 'full', component: MoviesListComponent },
      { path: 'create', component: MovieCreateComponent },
      { path: ':id', component: MoviesDetailComponent },
      { path: ':id/edit', component: MovieEditComponent }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MoviesRoutingModule {}
