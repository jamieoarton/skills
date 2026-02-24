# Get Filtered Team Tasks

View the tasks that meet specific criteria from a Workspace. Responses are limited to 100 tasks per page.  \
 \
You can only view task information of tasks you can access. \
 \
 Our Try It modal currently supports filtering by two or more Lists, Folders, or Spaces. To filter by a single List, Folder, or Space, we recommend using a free app like [Postman](https://www.postman.com/) to test our public API.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "ClickUp API v2 Reference",
    "description": "The ClickUp API enables you to programmatically access and manage your ClickUp resources.\n\n## Authentication\nThe API supports two authentication methods:\n- **Personal API Token**: Use for testing and personal integrations. Add token to requests with header: `Authorization: pk_...`\n- **OAuth 2.0**: Required for building apps for other users. Uses authorization code flow.\n\n## Getting Started\nOur [Getting Started Guide](https://developer.clickup.com/docs/index) provides a comprehensive overview of how to use the ClickUp API.\n",
    "contact": {},
    "version": "2.0"
  },
  "jsonSchemaDialect": "https://json-schema.org/draft/2020-12/schema",
  "servers": [
    {
      "url": "https://api.clickup.com/api",
      "description": "ClickUp",
      "variables": {}
    }
  ],
  "paths": {
    "/v2/team/{team_Id}/task": {
      "get": {
        "summary": "Get Filtered Team Tasks",
        "tags": [
          "Tasks"
        ],
        "description": "View the tasks that meet specific criteria from a Workspace. Responses are limited to 100 tasks per page.  \\\n \\\nYou can only view task information of tasks you can access. \\\n \\\n Our Try It modal currently supports filtering by two or more Lists, Folders, or Spaces. To filter by a single List, Folder, or Space, we recommend using a free app like [Postman](https://www.postman.com/) to test our public API.",
        "operationId": "GetFilteredTeamTasks",
        "parameters": [
          {
            "name": "team_Id",
            "in": "path",
            "description": "Workspace ID",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                123
              ]
            }
          },
          {
            "name": "page",
            "in": "query",
            "description": "Page to fetch (starts at 0).",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "contentEncoding": "int32"
            }
          },
          {
            "name": "order_by",
            "in": "query",
            "description": "Order by a particular field. By default, tasks are ordered by `created`.\\\n \\\nOptions include: `id`, `created`, `updated`, and `due_date`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "reverse",
            "in": "query",
            "description": "Tasks are displayed in reverse order.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "subtasks",
            "in": "query",
            "description": "Include or exclude subtasks. By default, subtasks are excluded.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "space_ids[]",
            "in": "query",
            "description": "Filter by Spaces. For example: \\\n \\\n`?space_ids[]=1234&space_ids[]=6789`",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "project_ids[]",
            "in": "query",
            "description": "Filter by Folders. For example: \\\n \\\n`?project_ids[]=1234&project_ids[]=6789`",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "list_ids[]",
            "in": "query",
            "description": "Filter by Lists. For example: \\\n \\\n`?list_ids[]=1234&list_ids[]=6789` ",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "statuses[]",
            "in": "query",
            "description": "Filter by statuses. Use `%20` to represent a space character. To include closed tasks, use the `include_closed` parameter. \\\n \\\nFor example: \\\n \\\n`?statuses[]=to%20do&statuses[]=in%20progress`",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "include_closed",
            "in": "query",
            "description": "Include or excluse closed tasks. By default, they are excluded.\\\n \\\nTo include closed tasks, use `include_closed: true`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "assignees[]",
            "in": "query",
            "description": "Filter by Assignees using people's ClickUp user id. For example: \\\n \\\n`?assignees[]=1234&assignees[]=5678`",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "tags[]",
            "in": "query",
            "description": "Filter by tags. User `%20` to represent a space character. For example: \\\n \\\n`?tags[]=tag1&tags[]=this%20tag`",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "due_date_gt",
            "in": "query",
            "description": "Filter by due date greater than Unix time in milliseconds.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "contentEncoding": "int64"
            }
          },
          {
            "name": "due_date_lt",
            "in": "query",
            "description": "Filter by due date less than Unix time in milliseconds.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "contentEncoding": "int64"
            }
          },
          {
            "name": "date_created_gt",
            "in": "query",
            "description": "Filter by date created greater than Unix time in milliseconds.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "contentEncoding": "int64"
            }
          },
          {
            "name": "date_created_lt",
            "in": "query",
            "description": "Filter by date created less than Unix time in milliseconds.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "contentEncoding": "int64"
            }
          },
          {
            "name": "date_updated_gt",
            "in": "query",
            "description": "Filter by date updated greater than Unix time in milliseconds.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "contentEncoding": "int64"
            }
          },
          {
            "name": "date_updated_lt",
            "in": "query",
            "description": "Filter by date updated less than Unix time in milliseconds.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "contentEncoding": "int64"
            }
          },
          {
            "name": "date_done_gt",
            "in": "query",
            "description": "Filter by date done greater than Unix time in milliseconds.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "contentEncoding": "int64"
            }
          },
          {
            "name": "date_done_lt",
            "in": "query",
            "description": "Filter by date done less than Unix time in milliseconds.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "contentEncoding": "int64"
            }
          },
          {
            "name": "custom_fields",
            "in": "query",
            "description": "Include tasks with specific values in one or more Custom Fields. Custom Relationships are included.\\\n \\\nFor example: `?custom_fields=[{\"field_id\":\"abcdefghi12345678\",\"operator\":\"=\",\"value\":\"1234\"}{\"field_id\":\"jklmnop123456\",\"operator\":\"<\",\"value\":\"5\"}]`\\\n \\\nOnly set Custom Field values display in the `value` property of the `custom_fields` parameter. The `=` operator isn't supported with Label Custom Fields.\\\n \\\nLearn more about [filtering using Custom Fields.](https://developer.clickup.com/docs/taskfilters)",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "parent",
            "in": "query",
            "description": "Include the parent task ID to return subtasks.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "include_markdown_description",
            "in": "query",
            "description": "To return task descriptions in Markdown format, use `?include_markdown_description=true`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean",
              "examples": [
                true
              ]
            }
          },
          {
            "name": "custom_items[]",
            "in": "query",
            "description": "Filter by custom task types. For example: \\\n \\\n`?custom_items[]=0&custom_items[]=1300` \\\n \\\nIncluding `0` returns tasks. Including `1` returns Milestones. Including any other number returns the custom task type as defined in your Workspace.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "array",
              "items": {
                "type": "number"
              }
            }
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "GetFilteredTeamTasksresponse",
                  "required": [
                    "tasks"
                  ],
                  "type": "object",
                  "properties": {
                    "tasks": {
                      "type": "array",
                      "items": {
                        "title": "Task3",
                        "required": [
                          "id",
                          "custom_id",
                          "name",
                          "text_content",
                          "description",
                          "status",
                          "orderindex",
                          "date_created",
                          "date_updated",
                          "date_closed",
                          "date_done",
                          "creator",
                          "assignees",
                          "watchers",
                          "checklists",
                          "tags",
                          "parent",
                          "priority",
                          "due_date",
                          "start_date",
                          "points",
                          "time_estimate",
                          "custom_fields",
                          "dependencies",
                          "linked_tasks",
                          "team_id",
                          "url",
                          "permission_level",
                          "list",
                          "project",
                          "folder",
                          "space"
                        ],
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string"
                          },
                          "custom_id": {
                            "type": [
                              "string",
                              "null"
                            ]
                          },
                          "name": {
                            "type": "string"
                          },
                          "text_content": {
                            "type": "string"
                          },
                          "description": {
                            "type": "string"
                          },
                          "markdown_description": {
                            "type": "string"
                          },
                          "status": {
                            "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D/get/responses/200/content/application~1json/schema/properties/status"
                          },
                          "orderindex": {
                            "type": "string"
                          },
                          "date_created": {
                            "type": "string"
                          },
                          "date_updated": {
                            "type": "string"
                          },
                          "date_closed": {
                            "type": "string"
                          },
                          "date_done": {
                            "type": [
                              "string",
                              "null"
                            ]
                          },
                          "creator": {
                            "title": "Creator5",
                            "required": [
                              "id",
                              "username",
                              "color",
                              "email",
                              "profilePicture"
                            ],
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "integer",
                                "contentEncoding": "int32"
                              },
                              "username": {
                                "type": "string"
                              },
                              "color": {
                                "type": "string"
                              },
                              "email": {
                                "type": "string"
                              },
                              "profilePicture": {
                                "type": "string"
                              }
                            },
                            "examples": [
                              {
                                "id": 123,
                                "username": "John Doe",
                                "color": "#000000",
                                "email": "johndoe@website.com",
                                "profilePicture": "https://clickup.com/avatar.jpg"
                              }
                            ]
                          },
                          "assignees": {
                            "type": "array",
                            "items": {
                              "title": "Assignees1",
                              "required": [
                                "id",
                                "username",
                                "color",
                                "email",
                                "profilePicture"
                              ],
                              "type": "object",
                              "properties": {
                                "id": {
                                  "type": "integer",
                                  "contentEncoding": "int32"
                                },
                                "username": {
                                  "type": "string"
                                },
                                "color": {
                                  "type": "string"
                                },
                                "email": {
                                  "type": "string"
                                },
                                "profilePicture": {
                                  "type": "string"
                                }
                              },
                              "examples": [
                                {
                                  "id": 123,
                                  "username": "John Doe",
                                  "color": "#000000",
                                  "email": "johndoe@website.com",
                                  "profilePicture": "https://clickup.com/avatar.jpg"
                                }
                              ]
                            },
                            "description": ""
                          },
                          "watchers": {
                            "type": "array",
                            "items": {
                              "title": "Watchers1",
                              "required": [
                                "id",
                                "username",
                                "color",
                                "email",
                                "profilePicture"
                              ],
                              "type": "object",
                              "properties": {
                                "id": {
                                  "type": "integer",
                                  "contentEncoding": "int32"
                                },
                                "username": {
                                  "type": "string"
                                },
                                "color": {
                                  "type": "string"
                                },
                                "email": {
                                  "type": "string"
                                },
                                "profilePicture": {
                                  "type": "string"
                                }
                              },
                              "examples": [
                                {
                                  "id": 123,
                                  "username": "John Doe",
                                  "color": "#000000",
                                  "email": "johndoe@website.com",
                                  "profilePicture": "https://clickup.com/avatar.jpg"
                                }
                              ]
                            },
                            "description": ""
                          },
                          "checklists": {
                            "type": "array",
                            "items": {
                              "title": "Checklists6",
                              "required": [
                                "id",
                                "task_id",
                                "name",
                                "date_created",
                                "orderindex",
                                "creator",
                                "resolved",
                                "unresolved",
                                "items"
                              ],
                              "type": "object",
                              "properties": {
                                "id": {
                                  "type": "string"
                                },
                                "task_id": {
                                  "type": "string"
                                },
                                "name": {
                                  "type": "string"
                                },
                                "date_created": {
                                  "type": "string"
                                },
                                "orderindex": {
                                  "type": "integer",
                                  "contentEncoding": "int32"
                                },
                                "creator": {
                                  "type": "integer",
                                  "contentEncoding": "int32"
                                },
                                "resolved": {
                                  "type": "integer",
                                  "contentEncoding": "int32"
                                },
                                "unresolved": {
                                  "type": "integer",
                                  "contentEncoding": "int32"
                                },
                                "items": {
                                  "type": "array",
                                  "items": {
                                    "$ref": "#/paths/~1v2~1checklist~1%7Bchecklist_id%7D~1checklist_item~1%7Bchecklist_item_id%7D/put/responses/200/content/application~1json/schema/properties/checklist/properties/items/items"
                                  },
                                  "description": ""
                                }
                              },
                              "examples": [
                                {
                                  "id": "d41340bc-2f17-43cc-ae71-86628f45825f",
                                  "task_id": "3cxv9f",
                                  "name": "Checklist",
                                  "date_created": "1618455803730",
                                  "orderindex": 1,
                                  "creator": 2770032,
                                  "resolved": 0,
                                  "unresolved": 1,
                                  "items": [
                                    {
                                      "id": "9398cb3d-55a4-4c45-ab46-2a47a371e375",
                                      "name": "checklist item 1",
                                      "orderindex": 0,
                                      "assignee": null,
                                      "resolved": false,
                                      "parent": null,
                                      "date_created": "1618455810454",
                                      "children": []
                                    }
                                  ]
                                }
                              ]
                            },
                            "description": ""
                          },
                          "tags": {
                            "type": "array",
                            "items": {
                              "$ref": "#/paths/~1v2~1team~1%7Bteam_Id%7D~1time_entries/post/requestBody/content/application~1json/schema/properties/tags/items"
                            },
                            "description": ""
                          },
                          "parent": {
                            "type": "string"
                          },
                          "priority": {
                            "type": "integer",
                            "contentEncoding": "int32"
                          },
                          "due_date": {
                            "type": "string"
                          },
                          "start_date": {
                            "type": "string"
                          },
                          "points": {
                            "type": "number"
                          },
                          "time_estimate": {
                            "type": "number"
                          },
                          "custom_fields": {
                            "type": "array",
                            "items": {
                              "title": "CustomFields9",
                              "required": [
                                "id",
                                "name",
                                "type",
                                "type_config",
                                "date_created",
                                "hide_from_guests",
                                "required"
                              ],
                              "type": "object",
                              "properties": {
                                "id": {
                                  "type": "string"
                                },
                                "name": {
                                  "type": "string"
                                },
                                "type": {
                                  "type": "string"
                                },
                                "type_config": {
                                  "type": "object"
                                },
                                "date_created": {
                                  "type": "string"
                                },
                                "hide_from_guests": {
                                  "type": "boolean"
                                },
                                "required": {
                                  "type": "boolean"
                                }
                              },
                              "examples": [
                                {
                                  "id": "be43f58e-989e-4233-9f25-27584f094b74",
                                  "name": "Location type Custom Field",
                                  "type": "location",
                                  "type_config": {},
                                  "date_created": "1617765143523",
                                  "hide_from_guests": false,
                                  "required": false
                                }
                              ]
                            },
                            "description": ""
                          },
                          "dependencies": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            },
                            "description": ""
                          },
                          "linked_tasks": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            },
                            "description": ""
                          },
                          "locations": {
                            "type": "array",
                            "items": {
                              "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D/get/responses/200/content/application~1json/schema/properties/locations/items"
                            },
                            "description": "Array of Lists where the task has been added."
                          },
                          "team_id": {
                            "type": "string"
                          },
                          "url": {
                            "type": "string"
                          },
                          "permission_level": {
                            "type": "string"
                          },
                          "list": {
                            "title": "List2",
                            "required": [
                              "id",
                              "name",
                              "access"
                            ],
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "string"
                              },
                              "name": {
                                "type": "string"
                              },
                              "access": {
                                "type": "boolean"
                              }
                            },
                            "examples": [
                              {
                                "id": "1752",
                                "name": "Shared with me",
                                "access": false
                              }
                            ]
                          },
                          "project": {
                            "title": "Project",
                            "required": [
                              "id",
                              "name",
                              "hidden",
                              "access"
                            ],
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "string"
                              },
                              "name": {
                                "type": "string"
                              },
                              "hidden": {
                                "type": "boolean"
                              },
                              "access": {
                                "type": "boolean"
                              }
                            },
                            "examples": [
                              {
                                "id": "1",
                                "name": "Folder",
                                "hidden": false,
                                "access": true
                              }
                            ]
                          },
                          "folder": {
                            "$ref": "#/paths/~1v2~1list~1%7Blist_id%7D/get/responses/200/content/application~1json/schema/properties/folder"
                          },
                          "space": {
                            "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D/get/responses/200/content/application~1json/schema/properties/space"
                          }
                        },
                        "examples": [
                          {
                            "id": "av1",
                            "custom_id": null,
                            "name": "My First Task",
                            "text_content": "Task description",
                            "description": "Task description",
                            "markdown_description": "Task description",
                            "status": {
                              "status": "Open",
                              "type": "open",
                              "orderindex": 1,
                              "color": "#000000"
                            },
                            "orderindex": "1.0000",
                            "date_created": "1508369194377",
                            "date_updated": "1508369194377",
                            "date_closed": "1508369194377",
                            "creator": {
                              "id": 123,
                              "username": "John Doe",
                              "color": "#000000",
                              "email": "johndoe@website.com",
                              "profilePicture": "https://clickup.com/avatar.jpg"
                            },
                            "assignees": [
                              {
                                "id": 123,
                                "username": "John Doe",
                                "color": "#000000",
                                "email": "johndoe@website.com",
                                "profilePicture": "https://clickup.com/avatar.jpg"
                              }
                            ],
                            "watchers": [
                              {
                                "id": 123,
                                "username": "John Doe",
                                "color": "#000000",
                                "email": "johndoe@website.com",
                                "profilePicture": "https://clickup.com/avatar.jpg"
                              }
                            ],
                            "checklists": [
                              {
                                "id": "d41340bc-2f17-43cc-ae71-86628f45825f",
                                "task_id": "3cxv9f",
                                "name": "Checklist",
                                "date_created": "1618455803730",
                                "orderindex": 1,
                                "creator": 2770032,
                                "resolved": 0,
                                "unresolved": 1,
                                "items": [
                                  {
                                    "id": "9398cb3d-55a4-4c45-ab46-2a47a371e375",
                                    "name": "checklist item 1",
                                    "orderindex": 0,
                                    "assignee": null,
                                    "resolved": false,
                                    "parent": null,
                                    "date_created": "1618455810454",
                                    "children": []
                                  }
                                ]
                              }
                            ],
                            "tags": [
                              {
                                "name": "tagged",
                                "tag_fg": "#000000",
                                "tag_bg": "#000000"
                              }
                            ],
                            "parent": "av2",
                            "priority": 1,
                            "due_date": "1508369194377",
                            "start_date": "1508369194377",
                            "points": 3,
                            "time_estimate": 1.2,
                            "custom_fields": [
                              {
                                "id": "be43f58e-989e-4233-9f25-27584f094b74",
                                "name": "Location type Custom Field",
                                "type": "location",
                                "type_config": {},
                                "date_created": "1617765143523",
                                "hide_from_guests": false,
                                "required": false
                              }
                            ],
                            "dependencies": [],
                            "linked_tasks": [],
                            "locations": [
                              {
                                "id": "123456",
                                "name": "Secondary List"
                              }
                            ],
                            "team_id": "1234",
                            "url": "https://app.clickup.com/t/av1",
                            "permission_level": "create",
                            "list": {
                              "id": "1",
                              "name": "List",
                              "access": true
                            },
                            "project": {
                              "id": "1",
                              "name": "Folder",
                              "hidden": false,
                              "access": true
                            },
                            "folder": {
                              "id": "1",
                              "name": "Folder",
                              "hidden": false,
                              "access": true
                            },
                            "space": {
                              "id": "1"
                            }
                          }
                        ]
                      },
                      "description": ""
                    }
                  },
                  "examples": [
                    {
                      "tasks": [
                        {
                          "id": "av1",
                          "custom_id": null,
                          "name": "My First Task",
                          "text_content": "Task description",
                          "description": "Task description",
                          "markdown_description": "Task description",
                          "status": {
                            "status": "Open",
                            "type": "open",
                            "orderindex": 1,
                            "color": "#000000"
                          },
                          "orderindex": "1.0000",
                          "date_created": "1508369194377",
                          "date_updated": "1508369194377",
                          "date_closed": "1508369194377",
                          "date_done": "1508369194377",
                          "creator": {
                            "id": 123,
                            "username": "John Doe",
                            "color": "#000000",
                            "email": "johndoe@website.com",
                            "profilePicture": "https://clickup.com/avatar.jpg"
                          },
                          "assignees": [
                            {
                              "id": 123,
                              "username": "John Doe",
                              "color": "#000000",
                              "email": "johndoe@website.com",
                              "profilePicture": "https://clickup.com/avatar.jpg"
                            }
                          ],
                          "watchers": [
                            {
                              "id": 123,
                              "username": "John Doe",
                              "color": "#000000",
                              "email": "johndoe@website.com",
                              "profilePicture": "https://clickup.com/avatar.jpg"
                            }
                          ],
                          "checklists": [
                            {
                              "id": "d41340bc-2f17-43cc-ae71-86628f45825f",
                              "task_id": "3cxv9f",
                              "name": "Checklist",
                              "date_created": "1618455803730",
                              "orderindex": 1,
                              "creator": 2770032,
                              "resolved": 0,
                              "unresolved": 1,
                              "items": [
                                {
                                  "id": "9398cb3d-55a4-4c45-ab46-2a47a371e375",
                                  "name": "checklist item 1",
                                  "orderindex": 0,
                                  "assignee": null,
                                  "resolved": false,
                                  "parent": null,
                                  "date_created": "1618455810454",
                                  "children": []
                                }
                              ]
                            }
                          ],
                          "tags": [
                            {
                              "name": "tagged",
                              "tag_fg": "#000000",
                              "tag_bg": "#000000"
                            }
                          ],
                          "parent": "av2",
                          "priority": 1,
                          "due_date": "1508369194377",
                          "start_date": "1508369194377",
                          "points": 3,
                          "time_estimate": 1.2,
                          "custom_fields": [
                            {
                              "id": "be43f58e-989e-4233-9f25-27584f094b74",
                              "name": "Location type Custom Field",
                              "type": "location",
                              "type_config": {},
                              "date_created": "1617765143523",
                              "hide_from_guests": false,
                              "required": false
                            }
                          ],
                          "dependencies": [],
                          "linked_tasks": [],
                          "locations": [
                            {
                              "id": "123456",
                              "name": "Secondary List"
                            }
                          ],
                          "team_id": "1234",
                          "url": "https://app.clickup.com/t/av1",
                          "permission_level": "create",
                          "list": {
                            "id": "1",
                            "name": "List",
                            "access": true
                          },
                          "project": {
                            "id": "1",
                            "name": "Folder",
                            "hidden": false,
                            "access": true
                          },
                          "folder": {
                            "id": "1",
                            "name": "Folder",
                            "hidden": false,
                            "access": true
                          },
                          "space": {
                            "id": "1"
                          }
                        }
                      ]
                    }
                  ]
                },
                "example": {
                  "tasks": [
                    {
                      "id": "av1",
                      "custom_id": null,
                      "name": "My First Task",
                      "text_content": "Task description",
                      "description": "Task description",
                      "markdown_description": "Task description",
                      "status": {
                        "status": "Open",
                        "type": "open",
                        "orderindex": 1,
                        "color": "#000000"
                      },
                      "orderindex": "1.0000",
                      "date_created": "1508369194377",
                      "date_updated": "1508369194377",
                      "date_closed": "1508369194377",
                      "date_done": "1508369194377",
                      "creator": {
                        "id": 123,
                        "username": "John Doe",
                        "color": "#000000",
                        "email": "johndoe@website.com",
                        "profilePicture": "https://clickup.com/avatar.jpg"
                      },
                      "assignees": [
                        {
                          "id": 123,
                          "username": "John Doe",
                          "color": "#000000",
                          "email": "johndoe@website.com",
                          "profilePicture": "https://clickup.com/avatar.jpg"
                        }
                      ],
                      "watchers": [
                        {
                          "id": 123,
                          "username": "John Doe",
                          "color": "#000000",
                          "email": "johndoe@website.com",
                          "profilePicture": "https://clickup.com/avatar.jpg"
                        }
                      ],
                      "checklists": [
                        {
                          "id": "d41340bc-2f17-43cc-ae71-86628f45825f",
                          "task_id": "3cxv9f",
                          "name": "Checklist",
                          "date_created": "1618455803730",
                          "orderindex": 1,
                          "creator": 2770032,
                          "resolved": 0,
                          "unresolved": 1,
                          "items": [
                            {
                              "id": "9398cb3d-55a4-4c45-ab46-2a47a371e375",
                              "name": "checklist item 1",
                              "orderindex": 0,
                              "assignee": null,
                              "resolved": false,
                              "parent": null,
                              "date_created": "1618455810454",
                              "children": []
                            }
                          ]
                        }
                      ],
                      "tags": [
                        {
                          "name": "tagged",
                          "tag_fg": "#000000",
                          "tag_bg": "#000000"
                        }
                      ],
                      "parent": "av2",
                      "priority": 1,
                      "due_date": "1508369194377",
                      "start_date": "1508369194377",
                      "points": 3,
                      "time_estimate": 1.2,
                      "custom_fields": [
                        {
                          "id": "be43f58e-989e-4233-9f25-27584f094b74",
                          "name": "Location type Custom Field",
                          "type": "location",
                          "type_config": {},
                          "date_created": "1617765143523",
                          "hide_from_guests": false,
                          "required": false
                        }
                      ],
                      "dependencies": [],
                      "linked_tasks": [],
                      "locations": [
                        {
                          "id": "123456",
                          "name": "Secondary List"
                        }
                      ],
                      "team_id": "1234",
                      "url": "https://app.clickup.com/t/av1",
                      "permission_level": "create",
                      "list": {
                        "id": "1",
                        "name": "List",
                        "access": true
                      },
                      "project": {
                        "id": "1",
                        "name": "Folder",
                        "hidden": false,
                        "access": true
                      },
                      "folder": {
                        "id": "1",
                        "name": "Folder",
                        "hidden": false,
                        "access": true
                      },
                      "space": {
                        "id": "1"
                      }
                    }
                  ]
                }
              }
            }
          }
        },
        "deprecated": false
      },
      "parameters": []
    }
  },
  "components": {
    "securitySchemes": {
      "Authorization_Token": {
        "name": "Authorization",
        "type": "apiKey",
        "in": "header",
        "description": "API token required for authentication. Two types of tokens are supported:\n**Personal API Key** Obtain from ClickUp's settings page under 'Apps' and add it to the header as `Authorization: pk_...`\n**OAuth2 Access Token** Generated through the OAuth2 flow and add it to the header as `Authorization: Bearer {access_token}`"
      }
    }
  },
  "security": [
    {
      "Authorization_Token": []
    }
  ],
  "tags": [
    {
      "name": "Tasks"
    }
  ]
}
```