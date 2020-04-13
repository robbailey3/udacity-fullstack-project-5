import { Actor } from '../actors/actor';
export interface Movie {
  id: number;
  title: string;
  release_date: Date;
  actors: Actor[];
  rating: number;
  synopsis: string;
}
