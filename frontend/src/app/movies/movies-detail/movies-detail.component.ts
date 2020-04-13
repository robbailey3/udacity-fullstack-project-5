import { Component, OnInit } from '@angular/core';
import { MoviesService } from '../movies.service';
import { ActivatedRoute, Params } from '@angular/router';
import { Movie } from '../movie';

@Component({
  selector: 'app-movies-detail',
  templateUrl: './movies-detail.component.html',
  styleUrls: ['./movies-detail.component.scss']
})
export class MoviesDetailComponent implements OnInit {
  public id: number;
  public movie: Movie;
  constructor(
    private readonly moviesService: MoviesService,
    private readonly route: ActivatedRoute
  ) {}

  ngOnInit(): void {
    this.getIdFromRoute();
  }

  public getIdFromRoute() {
    this.route.paramMap.subscribe((params: Params) => {
      this.id = params.get('id');
      this.getMovie();
    });
  }

  public getMovie() {
    this.moviesService
      .getMovieById(this.id)
      .subscribe({ next: (res: any) => (this.movie = res.result) });
  }
}
