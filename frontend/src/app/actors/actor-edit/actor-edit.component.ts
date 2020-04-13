import { Component, OnInit } from '@angular/core';
import { Actor } from '../actor';
import { ActorsService } from '../actors.service';
import { ActivatedRoute, Router, Params } from '@angular/router';
import { NotificationService } from '../../shared/notifications/notification.service';
import { Notification } from '../../shared/notifications/notification';
import { MoviesService } from '../../movies/movies.service';
import { Movie } from '../../movies/movie';

@Component({
  selector: 'app-actor-edit',
  templateUrl: './actor-edit.component.html',
  styleUrls: ['./actor-edit.component.scss']
})
export class ActorEditComponent implements OnInit {
  public actor: Partial<Actor> = {};
  public movies: Movie[];
  public id: number;
  constructor(
    private readonly route: ActivatedRoute,
    private readonly router: Router,
    private readonly actorsService: ActorsService,
    private readonly notificationService: NotificationService,
    private readonly moviesService: MoviesService
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
    this.actorsService.getActorByID(this.id).subscribe({
      next: (res: any) => {
        this.actor = res.result;
        console.log(this);
      }
    });
    this.moviesService.getMovies().subscribe({
      next: (res) => (this.movies = res.result),
      error: () => {}
    });
  }

  public submitForm() {
    this.actorsService.updateActor(this.id, this.actor).subscribe({
      next: () => {
        this.notificationService.addNotification(
          new Notification('Movie successfully added', 'success')
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
