import { Actor } from '../actors/actor';
export interface Agent {
  id: number;
  name: string;
  phone_number: string;
  email: string;
  actors: Actor[];
}
