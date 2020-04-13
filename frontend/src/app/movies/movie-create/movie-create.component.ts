import { Component, OnInit } from '@angular/core';
import { Movie } from '../movie';
import { MoviesService } from '../movies.service';
import { NotificationService } from '../../shared/notifications/notification.service';
import { Notification } from '../../shared/notifications/notification';
import { Router } from '@angular/router';

@Component({
  selector: 'app-movie-create',
  templateUrl: './movie-create.component.html',
  styleUrls: ['./movie-create.component.scss']
})
export class MovieCreateComponent {
  public movie: Partial<Movie> = {};
  constructor(
    private readonly moviesService: MoviesService,
    private readonly notificationService: NotificationService,
    private router: Router
  ) {}

  public submitForm() {
    this.moviesService.createMovie(this.movie).subscribe({
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
