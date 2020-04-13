import { Component, OnInit } from '@angular/core';
import { MoviesService } from '../movies/movies.service';
import { Movie } from '../movies/movie';
import { ActorsService } from '../actors/actors.service';
import { Actor } from '../actors/actor';

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.scss']
})
export class HomepageComponent implements OnInit {
  public movies: Movie[];
  public actors: Actor[];
  constructor(
    private readonly moviesService: MoviesService,
    private readonly actorsService: ActorsService
  ) {}

  public ngOnInit(): void {
    this.getMovies();
    this.getActors();
  }

  public getMovies() {
    this.moviesService.getMovies(3).subscribe({
      next: (res) => {
        this.movies = res.result;
      }
    });
  }

  public getActors() {
    this.actorsService.getActors(6).subscribe({
      next: (res) => {
        this.actors = res.result;
      }
    });
  }
}
