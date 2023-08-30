import kue from 'kue';
import { assert } from 'chai'; // Assuming you are using the chai assertion library
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue();
    queue.testMode.enter(); /* Enter test mode to prevent job processing */
  });

  afterEach(() => {
    queue.testMode.clear(); /* Clear the test queue and exit test mode */
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', () => {
    assert.throw(() => createPushNotificationsJobs(null, queue), 'Jobs is not an array');
  });

  it('should create new jobs in the queue', () => {
    const list = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 5678 to verify your account',
      },
      /* Add more job objects here... */
    ];

    createPushNotificationsJobs(list, queue);

    /* Assert that the correct number of jobs were added to the test queue */
    assert.equal(queue.testMode.jobs.length, list.length);

    /* 
     Assert specific job properties if needed
     For example: assert.equal(queue.testMode.jobs[0].data.phoneNumber, '4153518780');
     */
  });
});
