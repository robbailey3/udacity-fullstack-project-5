import { Component, OnInit } from '@angular/core';
import { ActorsService } from '../actors.service';
import { ActivatedRoute, Params } from '@angular/router';
import { Actor } from '../actor';
import { AuthService } from '../../auth/auth.service';

@Component({
  selector: 'app-actor-profile',
  templateUrl: './actor-profile.component.html',
  styleUrls: ['./actor-profile.component.scss']
})
export class ActorProfileComponent implements OnInit {
  public id;
  public actor: Actor;
  constructor(
    private readonly actorsService: ActorsService,
    public readonly authService: AuthService,
    private readonly route: ActivatedRoute
  ) {}

  public ngOnInit(): void {
    this.getIdFromRoute();
  }

  public getIdFromRoute() {
    this.route.paramMap.subscribe((params: Params) => {
      this.id = params.params.id;
    });
    this.getData();
  }
  public getData() {
    this.actorsService
      .getActorByID(this.id)
      .subscribe({ next: (res: any) => (this.actor = res.result) });
  }
}
