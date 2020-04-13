import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AuthService } from './auth.service';
import { UnauthenticatedComponent } from './unauthenticated/unauthenticated.component';
import { HTTP_INTERCEPTORS } from '@angular/common/http';
import { JWTInterceptor } from './interceptors/jwt.interceptor';

@NgModule({
  declarations: [UnauthenticatedComponent],
  imports: [CommonModule],
  providers: [
    AuthService,
    { provide: HTTP_INTERCEPTORS, useClass: JWTInterceptor, multi: true }
  ]
})
export class AuthModule {}
