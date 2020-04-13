import { Component, OnInit } from '@angular/core';
import { Notification } from '../../shared/notifications/notification';
import { Actor } from '../actor';
import { Movie } from 'src/app/movies/movie';
import { ActivatedRoute, Router, Params } from '@angular/router';
import { ActorsService } from '../actors.service';
import { NotificationService } from '../../shared/notifications/notification.service';
import { MoviesService } from '../../movies/movies.service';

@Component({
  selector: 'app-actor-create',
  templateUrl: './actor-create.component.html',
  styleUrls: ['./actor-create.component.scss']
})
export class ActorCreateComponent implements OnInit {
  public actor: Partial<Actor> = {};
  public movies: Movie[];
  public id: number;
  constructor(
    private readonly router: Router,
    private readonly actorsService: ActorsService,
    private readonly notificationService: NotificationService,
    private readonly moviesService: MoviesService
  ) {}
  public ngOnInit(): void {
    this.getData();
  }
  public getData() {
    this.moviesService.getMovies().subscribe({
      next: (res) => (this.movies = res.result),
      error: () => {}
    });
  }
  public submitForm() {
    this.actorsService.createActor(this.actor).subscribe({
      next: () => {
        this.notificationService.addNotification(
          new Notification('Actor successfully added', 'success')
        );
        this.router.navigateByUrl('/actors');
      },
      error: () => {
        this.notificationService.addNotification(
          new Notification('Something went wrong', 'error')
        );
      }
    });
  }
}
