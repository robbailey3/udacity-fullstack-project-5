export class Notification {
  constructor(
    public message: string,
    public type: 'success' | 'error' | 'info' = 'info',
    public timeout = 10000,
    public cancelable = true,
    public state: 'active' | 'inactive' = 'active'
  ) {
    if (this.state === 'active') {
      setTimeout(() => {
        this.state = 'inactive';
      }, timeout);
    }
  }
  public close() {
    this.state = 'inactive';
  }
}
