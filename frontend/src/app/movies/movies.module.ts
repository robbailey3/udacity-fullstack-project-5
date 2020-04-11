import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MoviesRootComponent } from './movies-root/movies-root.component';
import { MoviesListComponent } from './movies-list/movies-list.component';
import { MoviesDetailComponent } from './movies-detail/movies-detail.component';



@NgModule({
  declarations: [MoviesRootComponent, MoviesListComponent, MoviesDetailComponent],
  imports: [
    CommonModule
  ]
})
export class MoviesModule { }
