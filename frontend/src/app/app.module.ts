import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { GlobalModule } from './global/global.module';
import { SharedModule } from './shared/shared.module';
import { AuthModule } from './auth/auth.module';
import { ActorsModule } from './actors/actors.module';
import { AgentsModule } from './agents/agents.module';
import { MoviesModule } from './movies/movies.module';

@NgModule({
  declarations: [AppComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    GlobalModule,
    SharedModule,
    AuthModule,
    ActorsModule,
    AgentsModule,
    MoviesModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
