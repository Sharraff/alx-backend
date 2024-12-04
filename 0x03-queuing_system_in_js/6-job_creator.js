import kue from "kue";

const queue = kue.createQueue();

const data = {
    phoneNumber: 'string',
    message: 'string',
}

const job = queue.create("push_notification_code", data).save((err) => {
    if (!err) console.log("Notification jo created:", job.id);
});
job
    .on("complete", (result) => {
        console.log("Notification job completed");
    })
    .on("failed", (result) => {
        console.log("Notification job failed");
    });