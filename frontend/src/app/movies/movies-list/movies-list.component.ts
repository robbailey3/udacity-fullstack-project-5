import { Component, OnInit } from '@angular/core';
import { MoviesService } from '../movies.service';
import { Movie } from '../movie';
import { AuthService } from '../../auth/auth.service';
import { NotificationService } from '../../shared/notifications/notification.service';
import { Notification } from '../../shared/notifications/notification';

@Component({
  selector: 'app-movies-list',
  templateUrl: './movies-list.component.html',
  styleUrls: ['./movies-list.component.scss']
})
export class MoviesListComponent implements OnInit {
  public pageSize = 50;
  public offset = 0;
  public movies: Movie[];
  constructor(
    private readonly moviesService: MoviesService,
    public readonly authService: AuthService,
    private readonly notificationsService: NotificationService
  ) {}

  public ngOnInit(): void {
    this.getData();
  }

  public getData() {
    this.moviesService
      .getMovies(this.pageSize, this.offset)
      .subscribe({ next: (res) => (this.movies = res.result) });
  }

  public deleteMovie(id: number) {
    this.moviesService.deleteMovie(id).subscribe({
      next: (res) => {
        this.notificationsService.addNotification(
          new Notification(`Successfully deleted movie ${id}`, 'success')
        );
      },
      error: (err) => {
        this.notificationsService.addNotification(
          new Notification(
            'Ooops, something went wrong. Please try that again',
            'error'
          )
        );
      }
    });
  }
}
