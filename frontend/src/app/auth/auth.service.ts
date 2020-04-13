import { Injectable } from '@angular/core';
import { JwtHelperService } from '@auth0/angular-jwt';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private readonly url = environment.auth0.url;
  private readonly audience = environment.auth0.audience;
  private readonly clientId = environment.auth0.clientId;
  private readonly callbackURL = environment.auth0.callbackURL;
  private readonly JWT_STORAGE = 'JWT_KEY';
  private payload: any;
  public token: string;

  public loginLink(callbackPath = '') {
    // return `https://${this.url}.auth0.com/authorize?audience=${this.audience}&response_type=token&client_id=${this.clientId}&redirect_url=${this.callbackURL}${callbackPath}`;
    let link = 'https://';
    link += this.url + '.auth0.com';
    link += '/authorize?';
    link += 'audience=' + this.audience + '&';
    link += 'response_type=token&';
    link += 'client_id=' + this.clientId + '&';
    link += 'redirect_uri=' + this.callbackURL + callbackPath;
    return link;
  }

  public get isLoggedIn() {
    this.getToken();
    return this.token && !this.tokenHasExpired;
  }

  public getToken() {
    if (this.token && !this.tokenHasExpired) {
      return this.token;
    }
    // Token doesn't exist or it has expired
    this.token = this.getTokenFromLocalStorage();
    if (this.token && !this.tokenHasExpired) {
      return this.token;
    }
    this.token = this.getTokenFromURL();
    if (this.token && !this.tokenHasExpired) {
      return this.token;
    }
  }

  private getTokenFromLocalStorage() {
    return localStorage.getItem(this.JWT_STORAGE);
  }

  private getTokenFromURL() {
    const params = new URLSearchParams(window.location.hash.replace('#', '?'));
    return params.get('access_token');
  }

  public decodeToken() {
    const jwtService = new JwtHelperService();
    this.payload = jwtService.decodeToken(this.token);
  }

  public get tokenHasExpired() {
    if (!this.token || !this.payload) {
      return false;
    }
    return this.payload.exp / 1000 >= Date.now();
  }

  public hasPermission(permission: string) {
    this.decodeToken();
    return this.payload?.permissions?.includes(permission);
  }

  public logout() {
    this.token = null;
  }
}
