import { Component, OnInit } from '@angular/core';
import { Movie } from '../movie';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { MoviesService } from '../movies.service';

import { NotificationService } from '../../shared/notifications/notification.service';
import { Notification } from '../../shared/notifications/notification';

@Component({
  selector: 'app-movie-edit',
  templateUrl: './movie-edit.component.html',
  styleUrls: ['./movie-edit.component.scss']
})
export class MovieEditComponent implements OnInit {
  public movie: Partial<Movie> = {};
  public id: number;
  constructor(
    private readonly route: ActivatedRoute,
    private readonly router: Router,
    private readonly moviesService: MoviesService,
    private readonly notificationService: NotificationService
  ) {}

  public ngOnInit(): void {
    this.getIdFromRoute();
  }

  public getIdFromRoute() {
    this.route.paramMap.subscribe((params: Params) => {
      this.id = params.get('id');
      this.getData();
    });
  }

  public getData() {
    this.moviesService.getMovieById(this.id).subscribe({
      next: (res: any) => {
        this.movie = res.result;
        console.log(this);
      }
    });
  }

  public submitForm() {
    this.moviesService.updateMovie(this.id, this.movie).subscribe({
      next: () => {
        this.notificationService.addNotification(
          new Notification('Movie successfully added', 'success')
        );
        this.router.navigateByUrl('/movies');
      },
      error: () => {
        this.notificationService.addNotification(
          new Notification('Something went wrong', 'error')
        );
      }
    });
  }
}
