import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MoviesRootComponent } from './movies-root/movies-root.component';
import { MoviesListComponent } from './movies-list/movies-list.component';
import { MoviesDetailComponent } from './movies-detail/movies-detail.component';
import { HttpClientModule } from '@angular/common/http';
import { MoviesRoutingModule } from './movies-routing.module';
import { MovieEditComponent } from './movie-edit/movie-edit.component';
import { MovieCreateComponent } from './movie-create/movie-create.component';
import { SharedModule } from '../shared/shared.module';

@NgModule({
  declarations: [
    MoviesRootComponent,
    MoviesListComponent,
    MoviesDetailComponent,
    MovieEditComponent,
    MovieCreateComponent
  ],
  imports: [
    CommonModule,
    HttpClientModule,
    MoviesRoutingModule,
    FormsModule,
    SharedModule
  ]
})
export class MoviesModule {}
