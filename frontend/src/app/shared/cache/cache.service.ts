import { Injectable } from '@angular/core';
import { HttpResponse, HttpRequest } from '@angular/common/http';
import { CacheEntry } from './cache-entry';

/**
 * This class is for all Caching functionality of the application. This service
 * can be used to get and/or set cache entries.
 */
@Injectable({
  providedIn: 'root'
})
export class CacheService {
  /**
   * A Key => Value map for the cache.
   */
  public cache: Map<string, CacheEntry> = new Map();

  /**
   * The expiry time of the cache entry. This is currently set
   * to 5 minutes.
   */
  public cacheExpiry = 300000;

  /**
   * Add an entry to the cache.
   */
  public addToCache(req: HttpRequest<any>, response: HttpResponse<any>) {
    this.cache.set(req.urlWithParams, {
      response,
      expiry: Date.now() + this.cacheExpiry,
      params: req.params
    });
  }

  /**
   * Retrieve an entry from the cache. If no entry is found
   * for a given URL, this method returns `null`.
   */
  public get(req: HttpRequest<any>): HttpResponse<any> {
    if (!this.cache.has(req.urlWithParams)) {
      return null;
    }
    if (!this.cacheEntryIsValid(req)) {
      return null;
    }
    return this.cache.get(req.urlWithParams).response;
  }

  public removeCacheEntry(req: HttpRequest<any>): void {
    this.cache.delete(req.urlWithParams);
  }

  /**
   * Checks whether the cache entry is valid (i.e. whether more than 5 minutes has
   * elapsed since the item was added to the cache).
   * @param req
   * @returns `true` if the cache entry is valid. `false` otherwise.
   */
  private cacheEntryIsValid(req: HttpRequest<any>): boolean {
    if (this.cache.get(req.urlWithParams).expiry < Date.now()) {
      return true;
    } else {
      this.removeCacheEntry(req);
      return false;
    }
  }
}
