import {
  HttpInterceptor,
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpErrorResponse,
  HttpResponse
} from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';
import { filter, catchError } from 'rxjs/operators';
import { Injectable } from '@angular/core';

/**
 * An interceptor to append the OAuth2 Access Token
 * to each request.
 */
@Injectable()
export class JWTInterceptor implements HttpInterceptor {
  constructor(private service: AuthService, private router: Router) {}

  /**
   * This method is required by the HttpInterceptor.
   */
  public intercept(
    req: HttpRequest<any>,
    next: HttpHandler
  ): Observable<HttpEvent<any>> {
    if (this.service.token) {
      req = req.clone({
        headers: req.headers.set(
          'Authorization',
          `Bearer ${this.service.token}`
        )
      });
      console.log('HERE');
    }
    return next.handle(req);
  }
}
